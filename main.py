from fastapi import FastAPI
from uvicorn import run

app = FastAPI()

text = []

@app.post("/post_test")
def post_test(test:str):
    text.append(f"{test}")
    return text


@app.get("/get_test")
def get_test():
    return text


@app.delete("/delete_test")
def delete_test():
    text = []

if __name__ == "__main__":
    run(app=app)
