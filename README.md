## Overview
This project is a simple Movie Recommendation System that suggests movies based on a user's input. The system recommends movies by comparing the similarity between movies using Count Vectorization and Cosine Similarity techniques.

Given a movie title, the system identifies similar movies based on their plot descriptions or other metadata (like genres, keywords, etc.).

## Dataset
The dataset used for this project contains metadata about movies such as:

- Movie Id
- Title
- Tags
These features are used to calculate similarities between movies.

Dataset: https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

## Techniques Used
1. Count Vectorization: 
Converts text data (such as plot summaries or genres) into a matrix of token counts.
2. Cosine Similarity:
Measures the cosine of the angle between two non-zero vectors of an inner product space. It's used here to calculate similarity between two movies based on the count vectorized data.
