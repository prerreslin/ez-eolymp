from fastapi import FastAPI
from uvicorn import run

app = FastAPI()

@app.get("/get_test")
def get_test(test:str):
    with open("test.txt", "w") as file:
        file.write(f"{test}")


if __name__ == "__main__":
    run(app=app)
