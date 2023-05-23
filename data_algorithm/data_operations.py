import pandas as pd
from tools import convert, convert_cast, fetch_director, collapse

movies = pd.read_csv("tmdb_5000_movies.csv")
creds = pd.read_csv("tmdb_5000_credits.csv")

list_movies = movies.merge(creds, on="title")
new_list_movies = list_movies[["movie_id", "title", "overview", "genres", "keywords", "cast", "crew"]]
new_list_movies.dropna(inplace=True)

new_list_movies = new_list_movies.copy()
new_list_movies.loc[:, "genres"] = new_list_movies["genres"].apply(convert)
new_list_movies.loc[:, "keywords"] = new_list_movies["keywords"].apply(convert)
new_list_movies.loc[:, "cast"] = new_list_movies["cast"].apply(convert_cast)
new_list_movies.loc[:, "crew"] = new_list_movies["crew"].apply(fetch_director)

new_list_movies["cast"] = new_list_movies["cast"].apply(collapse)
new_list_movies["crew"] = new_list_movies["crew"].apply(collapse)
new_list_movies["genres"] = new_list_movies["genres"].apply(collapse)
new_list_movies["keywords"] = new_list_movies["keywords"].apply(collapse)

new_list_movies['overview'] = new_list_movies['overview'].apply(lambda x: x.split())

new_list_movies["tags"] = (
    new_list_movies["overview"]
    + new_list_movies["genres"]
    + new_list_movies["keywords"]
    + new_list_movies["cast"]
    + new_list_movies["crew"]
)

new_df = new_list_movies[["movie_id", "title", "tags"]]

new_df = new_df.copy()

new_df["tags"] = new_df["tags"].apply(lambda x: " ".join(x))
new_df["tags"] = new_df["tags"].apply(lambda x: x.lower())

print(new_df)
