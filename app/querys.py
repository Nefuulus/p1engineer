import pandas as pd
import numpy as np


amazon = pd.read_csv('datasets/amazon_prime_titles.csv',dtype = {'show_id': str},delimiter = ',',encoding = "utf-8")
disney = pd.read_csv('datasets/disney_plus_titles.csv',dtype = {'show_id': str},delimiter = ',',encoding = "utf-8")
hulu = pd.read_csv('datasets/hulu_titles.csv',dtype = {'show_id': str},delimiter = ',',encoding = "utf-8")
netflix = pd.read_json('datasets/netflix_titles.json',encoding = "utf-8")


amazon["Plataforma"] = "Amazon"
netflix["Plataforma"] = "Netflix"
hulu["Plataforma"] = "Hulu"
disney["Plataforma"] = "Disney"


frames = [amazon,disney,hulu,netflix]
movies = pd.concat(frames, ignore_index=True)

movies = movies.drop("country", axis = 1)
movies = movies.drop("description", axis = 1)
movies = movies.drop("date_added", axis = 1)
movies = movies.drop("director", axis = 1)
movies = movies.drop("rating", axis = 1)
movies = movies.drop("show_id", axis = 1)

movies["cast"] = movies["cast"].replace(np.nan, "Sin Datos")
movies["duration"] = movies["duration"].replace(np.nan, 0)


movies['duration'] = movies['duration'] .replace({'[a-zA-Z ]':''}, regex=True)

movies["duration"] = pd.to_numeric(movies["duration"])
movies["type"] = movies["type"].astype("string")
movies["title"] = movies["title"].astype("string")
movies["cast"] = movies["cast"].astype("string")

movies["duration_type"] =  np.where(movies["type"] == "Movie", "min", "season")

movies.rename(columns= {"type": "Tipo", "title" : "Titulo", "cast": "Actores", "release_year" : "Anio", "duration" : "Duracion", "listed_in": "Genero", "duration_type" : "Duracion_tipo"} , inplace= True)

