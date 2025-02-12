# -*- coding: utf-8 -*-
"""Updated movie recommendation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hURZRYyKGXs0DRedpgAx73zKrjMeo5ia

Importing dependencies
"""

import numpy as np
import pandas as pd
import difflib # User may  give the movie name slightly different than the real name to counter that issue this library is imported
from sklearn.feature_extraction.text import TfidfVectorizer # To convert texts to features , Tokenization
from sklearn.metrics.pairwise import cosine_similarity # For checking the similarity between movies

"""Data Pre-Processing"""

# Loading the dataset:
 movies_dataset = pd.read_csv('/content/drive/MyDrive/PROJECTS/Netflix Movie Recommendation/Datasets/updated dataset/movies.csv')

movies_dataset.head(5)

movies_dataset.shape

# Feature Selection
 selected_features = ['genres', 'keywords', 'tagline', 'cast', 'director']

# Replacing the missing values with NULL Strings
for feature in selected_features:
  movies_dataset[feature] = movies_dataset[feature].fillna('')

# Combining all the 5 Features:
combine_params = movies_dataset['genres']+' '+movies_dataset['keywords'] + ' ' + movies_dataset['tagline'] + ' '+movies_dataset['cast']+' '+movies_dataset['director']

combine_params.shape

combine_params.iloc[69]

# Converting text to feature vector
vectorizer = TfidfVectorizer() # Creating a object from tfid.. which will vectorize or text input in tfid algo

# Transforming text data in feature vectors
feature_vectors = vectorizer.fit_transform(combine_params)

print(feature_vectors)

# Cosine Similarity
similarity = cosine_similarity(feature_vectors)

print(similarity)

# Asking user for movie name
movie_name = input("Enter the Movie you've watched : ")

list_of_all_titles = movies_dataset['title'].tolist() # Converting into a list

# Just for clarification that the movie selected is present in the database or not
if 'The Notebook' in list_of_all_titles:
  print("present")

movie_name = input("Enter the Movie you've watched : ")

# Finding closest match for the user input movie
close_matched_movie = difflib.get_close_matches(movie_name, list_of_all_titles)

print(close_matched_movie)

"""Now we can see it's returning 3 possible matches 1st being the closest match lets choose the 1st element pf this list as the closest matched movie

"""

close_match = close_matched_movie[0]

print(close_match)

"""Now, we've the proper movie name that is present in the database. Let's find it's index"""

index_of_the_movie = movies_dataset[movies_dataset['title'] == close_match]['index']

print(index_of_the_movie)

"""Yields two indexes. So, let's select one of them"""

index_of_the_movie = index_of_the_movie.values[0]

print(index_of_the_movie)

# Finding similarirty confidence for each movie with the user input movie
similar_movies = list(enumerate(similarity[index_of_the_movie]))

print(similar_movies)

"""It basically yields similarity between the movie with all the other movies . Movies having Confidence value close to 1 will be much similar ."""

# sorting the movies based on their similarity confidence 
sorted_similar_movie = sorted(similar_movies, key = lambda x:x[1], reverse=True)
# Through the key part we're 1stly choosing the 2nd value of each tuple present in similar movies that is confidence value
# We want the sortng to be descending so reverse is assigned as True

print(sorted_similar_movie)

"""Now we can see movie having highest confidence value is shown at first and least at last So, our sorting is done.
From here we can easily say that movies that are close to the first element of the list will have much more similarity.
And by accessing the 1st element of the tuple we cam easily access the index of the similar movies.
Now, let's print the similar movie names
"""

print('Movies suggested for you : \n')

i = 1
for movie in sorted_similar_movie:
  ind = movie[0]
  title_from_index = movies_dataset[movies_dataset.index==ind]['title'].values[0]
  if(i <= 69):
    print(i,'.',title_from_index)
    i += 1

print("I will give you results even if you slightly mistype the movie name so Take A CHILL PILL.")
movie_name = input('Enter your favourite movie name : ')

list_of_all_titles = movies_dataset['title'].tolist()

find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles,1)
close_match = find_close_match[0]
print(f"Finding Similar movies for : {close_match}")
print("Don't Give 1 !!!")
choice = int(input("How many Similar movies do you want ? : "))
index_of_the_movie = movies_dataset[movies_dataset.title == close_match]['index'].values[0]

similar_movies = list(enumerate(similarity[index_of_the_movie]))

sorted_similar_movies = sorted(similar_movies, key = lambda x:x[1], reverse=True)

print('Movies suggested for you : \n')
i = 1
for movie in sorted_similar_movies:
  ind = movie[0]
  title_from_index = movies_dataset[movies_dataset.index==ind]['title'].values[0]
  if(i <= choice):
    if i == 1:
      print(f"{i}.{title_from_index}      (You can Re-watch it too 😉)")
    else:
      print(f"{i}.{title_from_index}")
    i += 1

