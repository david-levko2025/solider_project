from typing import Optional
from sqlmodel import Session, select, col
from models.agent import Agent

def create_agent(session:Session,id:int,name:str):
    agent = Agent(id=id,name=name)
    session.add(agent)
    session.commit()
    session.refresh(agent)
    print(f"created agent: ID:{agent.id} ,name:{agent.name}")
    return agent

def read_agent(session:Session):
    statement = select(Agent)
    agents = session.exec(statement).all()
    print(f"found {len(agents)} agents:")
    for agent in agents:
        print(f"(ID: {agent.id}) (name: {agent.name})")
    return agents

def search_agent_by_id(session:Session,id:Optional[int]):
    if id is None:
        print("ID cant be none")
        return None
    agent = session.get(Agent,id)
    if agent:
        print(f"agent found : (ID: {agent.id}) (name: {agent.name}") 
    else:
        print(f"agent with ID {id} not found")
    return agent

def search_agent_by_name(session:Session,name:str):
    if name is None:
        print("name cant be none")
        return None
    statement = select(Agent).where(Agent.name == name)
    agents = session.exec(statement).all()
    if agents:
        print(f" found {len(agents)} agents for name {name}")
        for agent in agents:
            print(f"agent found: ID {agent.id}, name {agent.name}")