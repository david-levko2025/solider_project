from typing import Optional
from sqlmodel import Field,SQLModel
from datetime import datetime, timezone


class Report(SQLModel, table = True):
    id : Optional[int] = False(default= None, primary_key= True)
    agent_id : Optional[int] = False(default= None, foriegn= True)
    terorist_id : Optional[int] = False(default= None, foriegn= True)
    create_at : datetime = Field(default_factory=lambda : datetime.now(timezone.utc))
    information : str 