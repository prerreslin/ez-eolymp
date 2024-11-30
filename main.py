from fastapi import FastAPI
from uvicorn import run
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,DeclarativeBase,Mapped,mapped_column

engine = create_engine("sqlite:///test.db")
Session = sessionmaker(bind=engine)

app = FastAPI()

class Base(DeclarativeBase):
    id:Mapped[int] = mapped_column(primary_key=True,autoincrement=True)

class Text(Base):
    __tablename__ = "text"
    text:Mapped[str] = mapped_column(nullable=True)

Text.metadata.drop_all(bind=engine)
Text.metadata.create_all(bind=engine)

@app.post("/post_test")
def post_test(test:str):
    with Session() as session:
        text = Text(
            text=test
        )
        session.add(text)
        session.commit()
        return text


@app.get("/get_test")
def get_test():
    with Session() as session:
        text = session.query(Text).all()
        return text


@app.delete("/delete_test")
def delete_test():
    with Session() as session:
        text = session.query(Text).delete()
        session.commit()
        return text

if __name__ == "__main__":
    run(app=app)
