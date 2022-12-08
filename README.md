# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

# <h1 align=center>**`Data Engineering`**</h1>

## Introducción:

¡Bienvenido! Este proyecto busca aplicar diferente herramientas de ETL para acercarnos al rol de un Data Engineer, y para ello se nos entregan 4 datasets con diferentes datos de peliculas y series a traves del tiempo. Los mismos pueden estar en formato csv o json y debemos realizar un EDA sobre cada uno y corregir imperfecciones como diferencias en el tipo de los datos, valores nulos, duplicados, etc.

## Objetivo: 

Realizar un trabajo de ETL sobre los datasets recibidos, luego, levantar una API con esos datos limpios a la que se le puedan realizar diferentes consultas.

Las consultas a realizar son:

+ Máxima duración según tipo de film (película/serie), por plataforma y por año.
    El request debe ser: get_max_duration(año, plataforma, [min o season])

+ Cantidad de películas y series (separado) por plataforma.
    El request debe ser: get_count_plataform(plataforma)  
  
+ Cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo.
    El request debe ser: get_listedin('genero')  

+ Actor que más se repite según plataforma y año.
    El request debe ser: get_actor(plataforma, año)

Plus: Realizar un deployment de la API en una plataforma "code to cloud" como por ejemplo, Mogenius.

## Explicación de los contenidos del Repositorio:

+ En el notebook `proyecto.ipynb` se encuentra el código comentado paso a paso, explicando las decisiones tomadas;
    Esto se hizo así para que cualquiera que quiera repasar el código pueda entender o editar el proceso.
    

+ En la carpeta `app` se encuentran los datasets analizados, el archivo `main.py` que es el archivo en el cual se configura FastAPI y se instancian los decoradores de la API y además, el archivo `querys.py` en el cual se encuentra el mismo código del notebook `proyecto.ipynb` pero más optimizado para subirlo a la nube y sin comentarios. De esta forma puedo tener mi código de una manera más resumida y de fácil acceso para importar en mi `main.py` que es donde se encuentran declaradas las funciones.

+ En el archivo `Dockerfile` se encuentra el entorno containerizado de Docker con FastAPI.



## Herramientas utilizadas:

+ Python.

+ Pandas.

+ Docker.

+ FastAPI.

+ HTML.