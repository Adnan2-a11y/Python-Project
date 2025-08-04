from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

URL="postgresql://postgres:DataBase123@127.0.0.1:5432/Room_Booking"
engine = create_engine(URL, echo = True)
Base = declarative_base()
SessionLocal = sessionmaker(bind = engine,autoflush=False,autocommit=False)

def get_db():
    db = SessionLocal()
    try:
        yield db
        
    finally:
        db.close()
