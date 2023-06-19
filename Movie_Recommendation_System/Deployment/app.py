import streamlit as st
import pickle
import pandas as pd
import requests

movies_dict = pickle.load(open('movies_dict', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load((open('similarity.pkl', 'rb')))


def fetch_poster(movie_id): #function for fetching image from tmdb-api
    url = "https://api.themoviedb.org/3/movie/{}?language=en-US".format(movie_id)
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer 'tmdb API Read Access Token' "}
    response = requests.get(url, headers=headers)
    data = response.json()
    # print(data)  #- just to see whether we are getting response or not
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie): # main function for recommending movies
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index] #cosine distance with other movies
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters



# creating front-end using streamlit
st.title('2Ez: Movie Recommender System')
selected_movie_name = st.selectbox('What movie do u have in mind?',movies_dict['title'].values())

if st.button('Recommend'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5) #streamlit component for displaying columns
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
