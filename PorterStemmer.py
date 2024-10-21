import nltk
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

def stem(text):
    y = []
    for i in text.split():
        y.append(ps.stem(i))
    return " ".join(y)   
  
new_df["tags"] = new_df["tags"].apply(stem)
new_df.head()

cv.get_feature_names_out()
