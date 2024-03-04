from fastapi import FastAPI
from uvicorn import run
from app import app_5


app = FastAPI()
app.mount('/homework_5/', app_5)  # монтирование подприложения app_5 в основное приложение app


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


if __name__ == '__main__':
    run("main:app", host='127.0.0.1', port=8000, reload=True)
