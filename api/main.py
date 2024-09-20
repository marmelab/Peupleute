from typing import Annotated
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/file-size/")
async def get_file_size(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}
