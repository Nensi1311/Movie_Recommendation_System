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

Movies.isnull().sum()
credits.isnull().sum()

Movies.info()
credits.info()
