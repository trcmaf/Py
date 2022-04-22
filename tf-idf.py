import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

dataset = [
    "New York times",
    "New York post new",
    "Los Angeles times post new post"
]

tfIdfVectorizer=TfidfVectorizer(use_idf=True)
tfIdf = tfIdfVectorizer.fit_transform(dataset)
df = pd.DataFrame(tfIdf[0].T.todense(), index=tfIdfVectorizer.get_feature_names(), columns=["TF-IDF"])
df = df.sort_values('TF-IDF', ascending=False)
print (df.head(25))