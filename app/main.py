from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()
from querys import movies

@app.get("/",response_class=HTMLResponse)
async def index():
    return """<html lang="en">
<head style = "color:blue;">
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Proyecto Individual N°1 - Data Engineering</title>
</head>
<body>
    <h1>Guía de usuario de la API</h1>
    <h3 style = "color: green;">/get_max_duration/AÑO/PLATAFORMA/TIPO Por ej: /get_max_duration/2020/netflix/min</h3>
    <p style = "color: blue; background-color:lightblue;">Devuelve la película/serie con mayor duración por plataforma, año y tipo de duración (min o seasons).</p>
    <h3>/get_count_platform/PLATAFORMA Por ej: /get_count_platform/disney</h3>
    <p>Devuelve la cantidad de películas y de series por plataforma</p>
    <h3>/get_listedin/GENERO Por ej: /get_listedin/comedy</h3>
    <p style ="color: red; background-color:blue;">Devuelve la cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo.</p>
    <h3>/get_actor/PLATAFORMA/AÑO Por ej: /get_actor/amazon/2020</h3>
    <p>Devuelve al actor/actriz con mayor número de apariciones según año y plataforma.</p>
    <h3>Luego de realizar alguna consulta, si desea volver a esta guía, elimine los decoradores.</h3>
</body>
</html>"""







@app.get("/get_max_duration/{anio}/{plataforma}/{min_o_season}")
def get_max_duration(anio, plataforma, min_o_season):

    
    if min_o_season == "min":
        x = movies[(movies["Anio"] == int(anio)) & (movies["Tipo"] == "Movie") & (movies["Plataforma"] == plataforma)]["Duracion"].max()
        y = (movies.loc[(movies["Anio"] == int(anio)) & (movies["Tipo"] == "Movie") & (movies["Plataforma"] == plataforma) & (movies["Duracion"] == x)]["Titulo"]).item()
        return f' {y} tiene la mayor duracion : con {x} {min_o_season}'
        

    if min_o_season == "season":
        x = movies[(movies["Anio"] == int(anio)) & (movies["Tipo"] == "TV Show") & (movies["Plataforma"] == plataforma)]["Duracion"].max()
        y = (movies.loc[(movies["Anio"] == int(anio)) & (movies["Tipo"] == "TV Show") & (movies["Plataforma"] == plataforma) & (movies["Duracion"] == x)]["Titulo"]).item()
        return f' {y} tiene la mayor duracion : con {x} {min_o_season}'
    else:
        return f'Datos incorrectos o faltantes para su consulta, intente nuevamente'


@app.get("/get_count_platform/{plataforma}")
def get_count_platform(plataforma):

    x =  movies[(movies["Tipo"] == "Movie") & (movies["Plataforma"] == plataforma )]["Titulo"].count()
    y =  movies[(movies["Tipo"] == "TV Show") & (movies["Plataforma"] == plataforma )]["Titulo"].count()

    return f' La plataforma, {plataforma}, tiene ,{x},peliculas y  {y} series'

@app.get("/get_listedin/{genero}")


def get_listedin(genero):

    a = 0

    for i in movies[(movies["Plataforma"] == "Amazon")]["Genero"]: 
            
        x = list(i.split(","))

        lista= []
        for names in x:
            lista.append(names.replace(" ",""))
        
        if genero in lista:
            a+=1

    
    b = 0

    for i in movies[(movies["Plataforma"] == "Hulu")]["Genero"]: 
            
        
        x = list(i.split(","))
        
        
        lista= []
        for names in x:
            lista.append(names.replace(" ",""))
        


        if genero in lista:
            b+=1

    
    c = 0

    for i in movies[(movies["Plataforma"] == "Netflix")]["Genero"]: 
            
        
        x = list(i.split(","))
        
        
        lista= []
        for names in x:
            lista.append(names.replace(" ",""))
        


        if genero in lista:
            c+=1
    d = 0

    for i in movies[(movies["Plataforma"] == "Disney")]["Genero"]: 
            
        
        x = list(i.split(","))
        
        
        lista= []
        for names in x:
            lista.append(names.replace(" ",""))
        


        if genero in lista:
            d+=1
    return f' El Genero, {genero}, aparece ,{a},veces en Amazon,{b} veces en Hulu, {c} veces en Netflix y {d} veces en Disney'
    


@app.get("/get_actor/{plataforma}/{anio}")
def get_actor(plataforma, anio):

 
    lista = []


    for i in movies[(movies["Plataforma"] == plataforma) & (movies["Anio"] == int(anio))]["Actores"]:
        x = list(i.split(","))
        
        for n in x:
            lista.append(n.strip())



    actoresunicos = []
    numero=[]
    mayor = 0
    for n in lista:
        if n == "Sin Datos":
            continue
        if n  in actoresunicos:
            indice = actoresunicos.index(n)
            numero[indice] += 1
        
        if not n in actoresunicos:
            actoresunicos.append(n)
            numero.append(1)
        

    for valor in numero:
        if valor > mayor:
            mayor = valor
    actorunico = actoresunicos[numero.index(mayor)]               
    return f'  La actriz con mas apariciones para el año {int(anio)} en la plataforma {plataforma} es {actorunico} con {mayor} apariciones '