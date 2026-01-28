# Movie Recommendation System
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
def load_movie_data(csv_file):
    """
    Load movie data from a CSV file.
    
    Args:
    csv_file (str): Path to the CSV file containing movie data.
    
    Returns:
    DataFrame: A pandas DataFrame containing the movie data.
    """
    return pd.read_csv(csv_file)
def compute_movie_similarities(movies_df):
    """
    Compute movie similarities based on their descriptions using TF-IDF and cosine similarity.
    
    Args:
    movies_df (DataFrame): A pandas DataFrame containing movie data with a 'description' column.
    
    Returns:
    DataFrame: A DataFrame containing similarity scores between movies.
    """
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(movies_df['description'].fillna(''))
    cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)
    return cosine_similarities
def get_recommendations(movie_title, movies_df, cosine_similarities, top_n=5):
    """Get movie recommendations based on a given movie title.
    Args:
    movie_title (str): The title of the movie for which to get recommendations.
    movies_df (DataFrame): A pandas DataFrame containing movie data.
    cosine_similarities (DataFrame): A DataFrame containing similarity scores between movies.
    top_n (int): The number of top recommendations to return.
    """
    if movie_title not in movies_df['title'].values:
        return f"Movie '{movie_title}' not found in the database."
    
    movie_idx = movies_df[movies_df['title'] == movie_title].index[0]
    similarity_scores = list(enumerate(cosine_similarities[movie_idx]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    similarity_scores = similarity_scores[1:top_n + 1]
    
    recommended_movie_indices = [i[0] for i in similarity_scores]
    return movies_df['title'].iloc[recommended_movie_indices].tolist()
# Example usage
if __name__ == '__main__':
    movies_df = load_movie_data('movies.csv')  # Ensure 'movies.csv' is in the same directory
    cosine_similarities = compute_movie_similarities(movies_df)
    
    movie_title = "The Matrix"
    recommendations = get_recommendations(movie_title, movies_df, cosine_similarities, top_n=5)
    print(f"Top recommendations for '{movie_title}':")
    for rec in recommendations:
        print(rec)
        