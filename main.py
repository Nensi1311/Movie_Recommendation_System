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

import ast
def convert(obj):
    l = []
    for i in ast.literal_eval(obj):
        l.append(i["name"])
    return l    
movies["genres"] = movies["genres"].apply(convert)
movies.head()
movies["keywords"] = movies["keywords"].apply(convert)
movies.head()

def convert_2(obj):
    l = []
    counter = 0
    for i in ast.literal_eval(obj):
        if counter != 3:
            l.append(i["name"])
            counter += 1
        else:
            break
    return l   
movies["cast"] = movies["cast"].apply(convert_2)
movies.head()

def fetch_director(obj):
    l = []
    for i in ast.literal_eval(obj):
        if i["job"] == "Director":
            l.append(i["name"])
            break
    return l 
movies["crew"] = movies["crew"].apply(fetch_director)   
movies.head()

movies["overview"] = movies["overview"].apply(lambda x : x.split())
movies.head()

movies["genres"] = movies["genres"].apply(lambda x : [i.replace(" ","") for i in x])
movies.head()

movies["keywords"] = movies["keywords"].apply(lambda x : [i.replace(" ","") for i in x])
movies.head()

movies["cast"] = movies["cast"].apply(lambda x : [i.replace(" ","") for i in x])
movies.head()

movies["crew"] = movies["crew"].apply(lambda x : [i.replace(" ","") for i in x])
movies.head()

movies["tags"] = movies["overview"] + movies["genres"] + movies["keywords"] + movies["cast"] + movies["crew"]
movies.head()

new_df = movies[["movie_id", "title", "tags"]]
new_df
new_df["tags"] = new_df["tags"].apply(lambda x : " ".join(x))
new_df.head()
new_df["tags"][0]
new_df["tags"] = new_df["tags"].apply(lambda x : x.lower())
new_df.head()


















Movies.isnull().sum()
credits.isnull().sum()

Movies.info()
credits.info()
