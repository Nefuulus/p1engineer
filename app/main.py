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
    <title>Proyecto Data Engineer Henry</title>
</head>
<body>
    <h1 style = "color:blue;"> Instrucciones de la API</h1>
    <h2 >Para realizar consultas se necesita poner lo siguiente:</h2>
    <h2 style = "color: red;" >www.DIRECCION.com/FUNCION/PARAMETRO1/PARAMETRO2 y asi sucesivamente segun corresponda</h2>
    <h2 style = "color:blue;"> Primera funcion: Esta funcion devuelve la máxima duración según tipo de film.</h2>
    <h2 style = "color: green;">Funcion : get_max_duration</h3>
    <h2 style = "color: green;">Parametro1 : Plataforma (puede ser Neflix, Disney, Hulu o Amazon)</h2>
    <h2 style = "color: green;">Parametro2 : Año (puede ser entre 1920 y 2021)</h2>
    <h2 style = "color: red;">Ejemplo : /get_max_duration/Netflix/1931</h2>
    
    <h2 style = "color:blue;"> Segunda funcion: Esta funcion devuelve la cantidad de peliculas y series segun la plataforma.</h2>
    <h2 style = "color: green;">Funcion : get_count_platform</h3>
    <h2 style = "color: green;">Parametro1 : Plataforma (puede ser Neflix, Disney, Hulu o Amazon)</h2>
    <h2 style = "color: red;">Ejemplo : /get_count_platform/Disney</h2>

    <h2 style = "color:blue;"> Tercera funcion: Esta funcion devuelve la cantidad de veces que se repite un género y plataforma con mayor fecuencia del mismo.</h2>
    <h2 style = "color: green;">Funcion : get_listedin</h3>
    <h2 style = "color: green;">Parametro1 : Genero (puede ser: Comedy, Documentary, Etc)</h2>
    <h2 style = "color: red;">Ejemplo : /get_listedin/Comedy</h2>
    <h2 style = "color:blue;"> Cuarta funcion: Esta funcion devuelve el actor que más se repite según plataforma y año.</h2>
    <h2 style = "color: green;">Funcion : get_actor</h3>
    <h2 style = "color: green;">Parametro1 : Plataforma (puede ser Neflix, Disney, Hulu o Amazon)</h2>
    <h2 style = "color: green;">Parametro2 : Año (puede ser entre 1920 y 2021)</h2>
    <h2 style = "color: red;">Ejemplo : /get_actor/Disney/2019</h2>
</body>
</html>"""







@app.get("/get_max_duration/{anio}/{plataforma}/{min_o_season}")
def get_max_duration(anio, plataforma, min_o_season):

    
    if min_o_season == "min":
        x = movies[(movies["Anio"] == int(anio)) & (movies["Tipo"] == "Movie") & (movies["Plataforma"] == plataforma)]["Duracion"].max()
        y = (movies.loc[(movies["Anio"] == int(anio)) & (movies["Tipo"] == "Movie") & (movies["Plataforma"] == plataforma) & (movies["Duracion"] == x)]["Titulo"]).item()
        return f' {y} tiene la mayor duracion : con {x} {min_o_season}/s'
        

    if min_o_season == "season":
        x = movies[(movies["Anio"] == int(anio)) & (movies["Tipo"] == "TV Show") & (movies["Plataforma"] == plataforma)]["Duracion"].max()
        y = (movies.loc[(movies["Anio"] == int(anio)) & (movies["Tipo"] == "TV Show") & (movies["Plataforma"] == plataforma) & (movies["Duracion"] == x)]["Titulo"]).item()
        return f' {y} tiene la mayor duracion : con {x} {min_o_season}/s'
    else:
        return f'Datos incorrectos o faltantes para su consulta, intente nuevamente'


@app.get("/get_count_platform/{plataforma}")
def get_count_platform(plataforma):

    x =  movies[(movies["Tipo"] == "Movie") & (movies["Plataforma"] == plataforma )]["Titulo"].count()
    y =  movies[(movies["Tipo"] == "TV Show") & (movies["Plataforma"] == plataforma )]["Titulo"].count()

    return f' La plataforma {plataforma} tiene : {x} peliculas y {y} series'

    

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
    return f' El Genero {genero} aparece {a} veces en Amazon, {b} veces en Hulu, {c} veces en Netflix y {d} veces en Disney'
    


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
    return f'La actriz con mas apariciones para el año {int(anio)} en la plataforma {plataforma} es {actorunico} con {mayor} aparicion/es '