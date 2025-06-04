import streamlit as st
import pickle
import pandas as pd
import requests
import time
import gdown
import os

# Load data
# URLs for your Google Drive files
movie_dict_url = "https://drive.google.com/uc?id=1xLzmW7_D64UtWpsEzPhuzens8Er39nXD"
similarity_url = "https://drive.google.com/uc?id=1AuUMLjpcXtR0RSXeOjz10QZITRY8K5k9"

# Download files only if not present
if not os.path.exists("movie_dict.pkl"):
    gdown.download(movie_dict_url, "movie_dict.pkl", quiet=False)

if not os.path.exists("similarity.pkl"):
    gdown.download(similarity_url, "similarity.pkl", quiet=False)

# Load the files
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))


# Fetch poster from TMDb

def fetch_poster(movie_id):
    try:
        api_key = os.environ.get("TMDB_API_KEY")
        if not api_key:
            raise ValueError("TMDB_API_KEY is not set in environment variables.")
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return "https://image.tmdb.org/t/p/w500" + data['poster_path']
    except Exception as e:
        st.warning(f"Error fetching poster: {e}")
        return "https://via.placeholder.com/500x750?text=No+Image"



# Recommendation function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))
        time.sleep(1)
    return recommended_movies, recommended_posters

# Streamlit UI
st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
    "Select a movie to get similar recommendations:",
    movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])

