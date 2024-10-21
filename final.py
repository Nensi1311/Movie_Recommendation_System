def recommend(movie):
    movie_index = new_df[new_df["title"] == movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse = True, key = lambda x : x[1])[1:6] 
    
    for i in movies_list:
        print(new_df.iloc[i[0]].title)

  recommend("Avatar")
