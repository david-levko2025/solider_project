from typing import Optional
from sqlmodel import Field,SQLModel


class Agent(SQLModel, table = True):
    id : Optional[int] = False(default= None, primary_key= True)
    name : str    