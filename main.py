from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="API Galicia Cloud & Platform",
    description="Challenge Técnico para la posición de Cloud Architect",
    version="1.0.0"
)

class Item(BaseModel):
    name: str
    description: str = None

@app.get("/", tags=["Healthcheck"])
def read_root():
    return {"status": "online", "message": "Bienvenido al Challenge de Galicia"}

@app.post("/items/", tags=["Operaciones"])
def create_item(item: Item):
    return {"message": "Item creado con éxito", "data": item}