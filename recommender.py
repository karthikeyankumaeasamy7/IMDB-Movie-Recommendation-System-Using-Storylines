import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset (scraped CSV from IMDb)
df = pd.read_csv("imdb_movies_2024.csv")

# Prepare TF-IDF on storylines
tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(df["Storyline"].fillna(""))

# Precompute cosine similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

def recommend_movies(storyline, top_n=5):
    """
    Recommend top_n similar movies based on storyline input text.
    Returns a DataFrame with Movie Name + Storyline.
    """
    if storyline.strip() == "":
        return pd.DataFrame(columns=["Movie Name", "Storyline"])

    # Transform input storyline
    input_vec = tfidf.transform([storyline])

    # Compute similarity
    sim_scores = cosine_similarity(input_vec, tfidf_matrix).flatten()

    # Get top_n indices
    top_indices = sim_scores.argsort()[::-1][:top_n]

    return df.iloc[top_indices][["Movie Name", "Storyline"]]