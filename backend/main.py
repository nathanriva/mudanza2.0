from fastapi import FastAPI
from functions import createArt, showAll, deleteArt, createBuy

app = FastAPI()

@app.get("/")
def home():
    return 'HOLA LINDO'

@app.get("/showart")
def showart():
    showAll()

@app.post("/newbuy")
def newbuy(id_compra, id_art, cant, in_stock):
    createBuy(id_compra, id_art, cant, in_stock)

@app.post("/newart")
def newart(name, id):
    createArt(name, id)

@app.delete('/deleteart')
def deleteart(idtodelete):
    deleteArt(idtodelete)