from typing import Annotated
from fastapi import FastAPI, File
from ..birdnet.analyze import identify

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/file-size/")
async def get_file_size(file: Annotated[bytes, File()]): # Stored in memory here
    return {"file_size": len(file)}

@app.post("/identify/")
async def identify_by_sound(record: Annotated[bytes, File()]):
    identifications = identify(record)
    return identifications
