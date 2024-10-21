from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 5000, stop_words = "english")

vectors = cv.fit_transform(new_df["tags"]).toarray()
vectors

cv.fit_transform(new_df["tags"]).toarray().shape
cv.get_feature_names_out()
len(cv.get_feature_names_out())
