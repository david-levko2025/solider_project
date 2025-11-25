from typing import Optional
from sqlmodel import Session, select, col
from models.terorist import Terorist

def create_terorist(session:Session,id:int,name:str):
    terorist = Terorist(id=id,name=name)
    session.add(terorist)
    session.commit()
    session.refresh(terorist)
    print(f"created terorist: ID:{terorist.id} ,name:{terorist.name}")
    return terorist

def read_report(session:Session):
    statement = select(Terorist)
    terorists = session.exec(statement).all()
    print(f"found {len(terorists)} terorists:")
    for terorist in terorists:
        print(f"(ID: {terorist.id}) (name: {terorist.agent_id})")
    return terorists

def search_terorist_by_id(session:Session,id:Optional[int]):
    if id is None:
        print("ID cant be none")
        return None
    terorist = session.get(Terorist,id)
    if terorist:
        print(f"terorist found : (ID: {terorist.id}) (name: {terorist.name}) ")
    else:
        print(f"terorist with ID {id} not found")
    return terorist

def search_terorist_by_name(session:Session,name:str):
    if name is None:
        print("name cant be none")
        return None
    statement = select(Terorist).where(Terorist.name == name)
    terorists = session.exec(statement).all()
    if terorist:
        print(f" found {len(terorists)} agents for name {name}")
        for terorist in terorists:
            print(f"agent found: ID {terorist.id}, name {terorist.namerorist}")