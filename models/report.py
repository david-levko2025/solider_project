from typing import Optional
from sqlmodel import Field,SQLModel


class Report(SQLModel, table = True):
    id : Optional[int] = False(default= None, primary_key= True)
    agent_id : Optional[int] = False(default= None, foriegn= True)
    terorist_id : Optional[int] = False(default= None, foriegn= True)
    datetime : 
    information : str 