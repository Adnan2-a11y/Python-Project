from sqlmodel import Field,SQLModel
from typing import Optional

class User(SQLModel, table=True):
    
    