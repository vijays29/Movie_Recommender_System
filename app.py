import pandas as pd
import streamlit as st

# Load the data
column_names = ['user_id', 'item_id', 'rating', 'timestamp']
df = pd.read_csv('src/file.tsv', sep='\t', names=column_names)
movie_titles = pd.read_csv('src/Movie_Id_Titles.csv')

# Merge the datasets
data = pd.merge(df, movie_titles, on='item_id')

# Calculate average ratings and number of ratings
ratings = pd.DataFrame(data.groupby('title')['rating'].mean())
ratings['num of ratings'] = data.groupby('title')['rating'].count()

# Create a pivot table
moviemat = data.pivot_table(index='user_id', columns='title', values='rating')

# Function to recommend movies based on correlation with a given movie
def recommend_movies(movie_name, min_ratings=100):
    movie_user_ratings = moviemat[movie_name]
    similar_to_movie = moviemat.corrwith(movie_user_ratings)

    corr_movie = pd.DataFrame(similar_to_movie, columns=['Correlation'])
    corr_movie.dropna(inplace=True)
    corr_movie = corr_movie.join(ratings['num of ratings'])
    recommendations = corr_movie[corr_movie['num of ratings'] > min_ratings].sort_values('Correlation', ascending=False)
    return recommendations

# Streamlit frontend
st.title('Movie Recommendation System')

# User input for the movie title
movie_name = st.selectbox('Select a movie to get recommendations:', ratings.index)

# Slider to set the minimum number of ratings for recommendations
min_ratings = st.slider('Minimum number of ratings', min_value=50, max_value=500, value=100)

# Recommend movies
if movie_name:
    recommendations = recommend_movies(movie_name, min_ratings)
    
    if not recommendations.empty:
        st.subheader(f"Movies similar to '{movie_name}':")
        for title, row in recommendations.head(10).iterrows():
            st.write(f"{title} (Correlation: {row['Correlation']:.2f}, Ratings: {row['num of ratings']})")
    else:
        st.write("No recommendations found.")
