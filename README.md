# Movie Recommendation System

This is a simple Movie Recommendation System built using Streamlit and Pandas. The system provides recommendations based on movie ratings and correlations between user ratings of different movies.

## Features

- Select a movie to receive recommendations for similar movies.
- Control the minimum number of ratings required for movie recommendations.
- Get recommendations based on user ratings correlations.

## Data Sources

- **User ratings dataset**: The dataset contains movie ratings from users, which are used to build the recommendation system.
- **Movie titles dataset**: This dataset provides the mapping of movie IDs to their respective titles.

## Requirements
   - Python 3.x
   - Required Python libraries (can be installed via requirements.txt):
        - pandas
        - streamlit

## Installation

To run Vonic locally, follow these steps:

1. Clone the repository:
   
   ```
   git clone https://github.com/vijays29au/movie_recommendor.git
   ```


2. Navigate to the project directory:

   ```
   cd movie_recommendor
   ```

3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Run the application:

   ```
   streamlit run app.py
   ```

   The Streamlit server will start, and you can access the application by navigating to the URL provided in the terminal.

## How It Works

   1. The application loads movie rating data and calculates the average rating and the number of ratings for each movie.
   2. A correlation matrix is built based on user ratings for each movie.
   3. The user selects a movie from a dropdown, and the app displays recommendations for movies with similar ratings, based on correlation.
   4. A slider allows the user to adjust the minimum number of ratings required for recommendations.

## Example

   1. Select a movie, for example, "Star Wars (1977)".
   2. Adjust the minimum number of ratings using the slider.
   3. The app will display movies similar to "Star Wars (1977)", along with the correlation score and the number of ratings for each recommended movie.
    
## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or support, please contact [vijays003729@gmail.com](mailto:vijays003729@gmail.com).
