from fastapi import FastAPI
from uvicorn import run

app = FastAPI()

text = ""

@app.post("/post_test")
def post_test(test:str):
    text = test
    return text


@app.get("/get_test")
def get_test():
    return text


if __name__ == "__main__":
    run(app=app)
