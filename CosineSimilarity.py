from sklearn.metrics.pairwise import cosine_similarity
similarity = cosine_similarity(vectors)
similarity 

similarity[0] # diagonal similarity is always 1
similarity[1]
similarity = cosine_similarity(vectors).shape
similarity

sorted(list(enumerate(similarity[0])), reverse = True, key = lambda x : x[1])[1:6] # sorted by distance
