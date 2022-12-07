from fastapi import FastAPI
app = FastAPI()
from fastapi.responses import HTMLResponse
from querys import movies

@app.get("/")
def read_root():
    return{"hello" : "World23333323"}
