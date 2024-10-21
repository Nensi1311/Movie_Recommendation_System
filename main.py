# import libraries
import numpy as np
import pandas as pd

# data loading
Movies = pd.read_csv("tmdb_5000_movies.csv")
Movies
credits = pd.read_csv("tmdb_5000_credits.csv")
credits

Movies.head()
credits.head()

Movies.describe()
credits.describe()

# EDA 
movies = Movies.merge(credits, on = "title")
movies
movies.head()
movies.describe()
movies.describe(include = "object")
movies.shape
movies.info()
movies.isnull().sum()
movies["original_language"].value_counts()
movies.drop(columns = ["budget", "homepage", "original_language", "original_title", "popularity", "production_companies", "production_countries", "release_date", "revenue", "runtime", "spoken_languages", "tagline", "vote_average", "vote_count", "id", "status"], axis = 0, inplace = True)
movies.head()
movies = movies[["movie_id", "title", "overview", "genres", "keywords", "cast", "crew"]]
movies.head()
movies.isnull().sum()
movies.dropna(inplace = True)
movies.isnull().sum()
movies.duplicated().sum()
movies.iloc[0].genres























Movies.isnull().sum()
credits.isnull().sum()

Movies.info()
credits.info()
