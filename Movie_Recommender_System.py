#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


Movies = pd.read_csv("tmdb_5000_movies.csv")
Movies


# In[3]:


credits = pd.read_csv("tmdb_5000_credits.csv")
credits


# In[4]:


Movies.head()


# In[5]:


credits.head()


# In[6]:


Movies.describe()


# In[7]:


credits.describe()


# In[8]:


Movies.isnull().sum()


# In[9]:


credits.isnull().sum()


# In[10]:


Movies.info()


# In[11]:


credits.info()


# In[12]:


movies = Movies.merge(credits, on = "title")
movies


# In[13]:


movies.head()


# In[14]:


movies.describe()


# In[15]:


movies.describe(include = "object")


# In[16]:


movies.shape


# In[17]:


movies.info()


# In[18]:


movies.isnull().sum()


# In[19]:


movies["original_language"].value_counts()


# In[20]:


movies.drop(columns = ["budget", "homepage", "original_language", "original_title", "popularity", "production_companies", "production_countries", "release_date", "revenue", "runtime", "spoken_languages", "tagline", "vote_average", "vote_count", "id", "status"], axis = 0, inplace = True)


# In[21]:


movies.head()


# In[22]:


movies = movies[["movie_id", "title", "overview", "genres", "keywords", "cast", "crew"]]


# In[23]:


movies.head()


# In[24]:


movies.isnull().sum()


# In[25]:


movies.dropna(inplace = True)


# In[26]:


movies.isnull().sum()


# In[27]:


movies.duplicated().sum()


# In[29]:


movies.iloc[0].genres


# In[32]:


import ast


# In[33]:


def convert(obj):
    l = []
    for i in ast.literal_eval(obj):
        l.append(i["name"])
    return l    


# In[34]:


movies["genres"] = movies["genres"].apply(convert)


# In[35]:


movies.head()


# In[36]:


movies["keywords"] = movies["keywords"].apply(convert)


# In[37]:


movies.head()


# In[38]:


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


# In[40]:


movies["cast"] = movies["cast"].apply(convert_2)


# In[41]:


movies.head()


# In[42]:


def fetch_director(obj):
    l = []
    for i in ast.literal_eval(obj):
        if i["job"] == "Director":
            l.append(i["name"])
            break
    return l 


# In[43]:


movies["crew"] = movies["crew"].apply(fetch_director)


# In[44]:


movies.head()


# In[45]:


movies["overview"] = movies["overview"].apply(lambda x : x.split())


# In[46]:


movies.head()


# In[47]:


movies["genres"] = movies["genres"].apply(lambda x : [i.replace(" ","") for i in x])


# In[48]:


movies.head()


# In[49]:


movies["keywords"] = movies["keywords"].apply(lambda x : [i.replace(" ","") for i in x])


# In[50]:


movies.head()


# In[51]:


movies["cast"] = movies["cast"].apply(lambda x : [i.replace(" ","") for i in x])


# In[52]:


movies.head()


# In[53]:


movies["crew"] = movies["crew"].apply(lambda x : [i.replace(" ","") for i in x])


# In[54]:


movies.head()


# In[55]:


movies["tags"] = movies["overview"] + movies["genres"] + movies["keywords"] + movies["cast"] + movies["crew"]


# In[56]:


movies.head()


# In[57]:


new_df = movies[["movie_id", "title", "tags"]]
new_df


# In[58]:


new_df["tags"] = new_df["tags"].apply(lambda x : " ".join(x))


# In[59]:


new_df.head()


# In[60]:


new_df["tags"][0]


# In[61]:


new_df["tags"] = new_df["tags"].apply(lambda x : x.lower())


# In[62]:


new_df.head()


# In[63]:


from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 5000, stop_words = "english")


# In[66]:


vectors = cv.fit_transform(new_df["tags"]).toarray()
vectors


# In[67]:


cv.fit_transform(new_df["tags"]).toarray().shape


# In[70]:


cv.get_feature_names_out()


# In[71]:


len(cv.get_feature_names_out())


# In[72]:


import nltk


# In[73]:


from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()


# In[74]:


def stem(text):
    y = []
    for i in text.split():
        y.append(ps.stem(i))
    return " ".join(y)    


# In[75]:


new_df["tags"] = new_df["tags"].apply(stem)


# In[76]:


new_df.head()


# In[78]:


cv.get_feature_names_out()


# In[80]:


from sklearn.metrics.pairwise import cosine_similarity


# In[84]:


similarity = cosine_similarity(vectors)
similarity 


# In[86]:


similarity[0] # diagonal similarity is always 1


# In[87]:


similarity[1]


# In[83]:


similarity = cosine_similarity(vectors).shape
similarity


# In[90]:


sorted(list(enumerate(similarity[0])), reverse = True, key = lambda x : x[1])[1:6] # sorted by distance


# In[93]:


def recommend(movie):
    movie_index = new_df[new_df["title"] == movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse = True, key = lambda x : x[1])[1:6] 
    
    for i in movies_list:
        print(new_df.iloc[i[0]].title)


# In[94]:


recommend("Avatar")


# In[ ]:




