#This creates a new FastAPI app, with two endpoints: /, which returns a simple "Hello World" message, and /bark/{prompt}, 
#which receives a prompt parameter as part of the URL, 
#sends it to the Bark repository for processing via a POST request, and returns the result as a JSON response.

from fastapi import FastAPI
import requests

app = FastAPI()

BARK_URL = "https://api.suno.ai/bark/prompt"

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/bark/{prompt}")
def bark(prompt: str):
    response = requests.post(BARK_URL, json={"prompt": prompt})
    return response.json()

  
  
