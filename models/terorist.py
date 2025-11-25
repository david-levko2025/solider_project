from typing import Optional
from sqlmodel import Field,SQLModel,Relationship



class Terorist(SQLModel, table = True):
    id : Optional[int] = False(default= None, primary_key= True)
    name : str = Field(index=True) 


    reports : list["Reports"] = Relationship(back_populates="terorist")
   