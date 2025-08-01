from sqlmodel import SQLModel, create_engine

DATABASE_URL = "postgresql://postgres:DataBase123@127.0.0.1:5432/postgres"
engine=create_engine(DATABASE_URL, echo=True)

def create_db():
    SQLModel.metadata.create_all(engine)
