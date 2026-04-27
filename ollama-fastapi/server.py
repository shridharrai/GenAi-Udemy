from fastapi import FastAPI, Body
from ollama import Client

app = FastAPI()
client = Client()


@app.get("/")
def read_root():
    return {"Hello": "Shridhar"}


@app.post("/chat")
def chat(message: str = Body(..., description="The Message")):
    response = client.chat(
        model="gemma:2b", messages=[{"role": "user", "content": message}]
    )
    return {"response": response.message.content}
