from datetime import datetime
import json


class Agent:
    def __init__(self, name):
        self.name = name
        self.connected = False
        self.login_time = None

    def connect(self):
        self.connected = True
        self.login_time = datetime.now()

    def disconnect(self):
        self.connected = False


class AgentManager:
    def __init__(self):
        self.agents = {}

    def add_agent(self, name):
        if name not in self.agents:
            self.agents[name] = Agent(name)

    def connect_agent(self, name):
        if name not in self.agents:
            self.add_agent(name)
        self.agents[name].connect()
        return self.agents[name].login_time

    def disconnect_agent(self, name):
        if name in self.agents:
            self.agents[name].disconnect()

    def get_connected_agents(self):
        for a in self.agents.values():
            if a.connected:
                return a.name

    # def get_connected_agents(self):     
    #     return [a.name for a in self.agents.values() if a.connected]
    #             ---potential in place---

class DataLogger:
    @staticmethod
    def log_login(name, login_time, file="logins.json"):
        try:
            with open(file, "r") as f:
                data = json.load(f)
        except:
            data = []

        data.append({
            "agent": name,
            "login_time": str(login_time)
        })

        with open(file, "w") as f:
            json.dump(data, f, indent=4)




manager = AgentManager()

login_time = manager.connect_agent("David")
DataLogger.log_login("David", login_time)


print("connected:", manager.get_connected_agents())


manager.disconnect_agent("David")
