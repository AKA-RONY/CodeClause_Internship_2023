
# 2Ez: Movie Recommendation System 
## What is a Recommendation System?
A recommender system is a software program/web-application that consist of complex logics & ML-Algorithms, which understands human behaviour and interest, and based on that it recommends the products or services.\
**Example**- **Amazon** uses recommendation system for showing products based on user preferences, **Netflix**, **Amazon Prime** suggest movies to watch as recommendation etc.
## Types of Recommendation System
 **Content Based Filtering**:
- Content-based filtering recommends items to users based on the characteristics and properties of the items themselves.
- It analyzes the content features or attributes of the items, such as genre, actors, directors, or plot keywords, and compares them to the user's preferences.
- For example, in a music recommendation system, if a user has shown a preference for rock music, the content-based approach would suggest other songs or artists in the rock genre based on their shared characteristics.

**Collaborative Based Filtering**:
- Collaborative filtering recommends items to users based on the behavior and preferences of other similar users.
- It looks for patterns and similarities among users' past interactions or ratings and identifies users with similar tastes or preferences.
- For example, in a movie recommendation system, if User A and User B have similar movie preferences and User A rates a movie highly, collaborative filtering would recommend that movie to User B because of their shared tastes.

**Hybrid (Content + Collaborative) Filtering:**
- Hybrid recommendation systems combine content-based and collaborative filtering approaches to leverage their respective strengths.
- These systems aim to improve recommendation quality by integrating multiple techniques.
- Different hybridization techniques can be employed, such as weighted combination, switching, feature combination, or cascade.


# Project Overview
The Content-Based Movie Recommendation System is a project aimed at providing personalized movie recommendations based on the content and characteristics of movies. It utilizes machine learning and natural language processing (NLP) techniques to analyze movie attributes and generate recommendations for users. The system primarily focuses on the content of movies, such as genre, actors, directors, and plot summaries, to suggest similar movies that users are likely to enjoy.

# Approach
- **Data Gathering/collection** -https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata
- **Data Pre-processing** - making the data in a format that is correct and useful to us ; like cleaning it, restructuring it, etc. 
- **Model Development** - Performed stemming, text vectorization, cosine-similarity
- **Creating Front-end** - used Streamlit components
- **Deployment** - Streamlit Community Cloud




## Screenshots
![Screenshot (343)](https://github.com/salvik43/Power-BI_Dashboard_Project/assets/67736824/70e860bb-f71a-49b8-a4eb-8a4a83a89a02)

![Screenshot (344)](https://github.com/salvik43/Power-BI_Dashboard_Project/assets/67736824/bf1e328c-4797-4c5b-8c47-a85a8adc1747)

![Screenshot (345)](https://github.com/salvik43/Power-BI_Dashboard_Project/assets/67736824/64d2784c-a8bf-4b04-aaa4-cbb8994e4980)


## Tools & Libraries
- virtualenv
- jupyter Notebook,Pycharm community
- python 3.9 or above
- pandas
- numpy
- streamlit 
- requests
- pickle
- scikit-learn
- nltk





## Installation

Installing Virtual Environment

```bash
  pip install virtualenv
```
Creating Virtual Environment

```bash
  virtualenv environment_name
  or
  python -m venv environment_name
```
Activating Virtual Environment

```bash
  environment_name\scripts\activate 
```
Installing Dependencies after Activating venv

```bash
  pip install -r requirements.txt
```
deactivating venv
```bash
  deactivate
```
## Starting Dev server

After installing all the dependencies and getting the 'API-Read Access-Token' from TMDB website , you can run the application in your local machine by executing the command in the root directory 

```bash
  streamlit run app.py
```


## Conclusion
Though the main aim for this project is accomplished i.e generating recommendation for the movies. But the model still needs fine-tuning and has further scope for improvement. Like optimizing  the search results, adding more sections (reviews,movie description, etc.) I tried deploying it using AWS EC2,render, it worked fine but found streamlit community cloud a better pick for this project as for its simple deployment process and better support for streamlit apps.
## Demo


https://github.com/salvik43/Power-BI_Dashboard_Project/assets/67736824/0d94d7f0-aa65-40ee-b32f-2942d5ac1180




