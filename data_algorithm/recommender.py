from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
from data_operations import new_df

cv = CountVectorizer(max_features=5000, stop_words="english")
vector = cv.fit_transform(new_df["tags"]).toarray()
similarity = cosine_similarity(vector)


def recommend(movie):
    index = new_df[new_df["title"] == movie].index[0]
    distances = sorted(
        list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1]
    )
    for i in distances[1:6]:
        print(new_df.iloc[i[0]].title)


pickle.dump(new_df, open("movie_list.pkl", "wb"))
