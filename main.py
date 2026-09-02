from fastapi import FastAPI

Webapp = FastAPI()

@Webapp.get("/")
def home():
    return {"message":"Hello World"}