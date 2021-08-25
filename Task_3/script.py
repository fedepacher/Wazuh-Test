from agent import Agent
from pathlib import Path
import json

MAX_RANGE_AGENT = 6         #maximun number of agents
MIN_RANGE_AGENT = 1         #minimuim number of agents

class Script:

    '''
    Constructor of the Script class
    '''
    def __init__(self) -> None:
        pass

    '''
    Function that read a json file of agents and add a new agent. 
    Create an output json file with the new list of agents 
    Print an agent or the new agent's list 
    param agentN    agent to be printed if it is in the range of MIN_RANGE_AGENT 
                    and MAX_RANGE_AGENT. If it is None print the full list
    '''
    def runScript(self, agentN=None):
        try:
            fileInfo = self.loadAgent('data.json')
        except FileNotFoundError:
            print("Wrong file or file path")
            exit()

        agents_list = []
        for element in fileInfo:
            agent = Agent(element['id'], element['name'], element['version'], element['os']
            , element['inventory'], element['modules'], element['status'])
            agents_list.append(agent)

        new_agent = Agent(6, "agent_6", "4.1.3", "mac", ["vmware", "git", "atom"], 
            {
                "fim": {"status": "enabled", "frequency": 15, "eps": 100},
                "syscollector": {"status": "enabled", "frequency": 22, "eps": 30},
                "rootcheck": {"status": "enabled", "frequency": 15, "eps": 50},
                "winevt": {"status": "enabled", "frequency": 25, "eps": 180},
                "logcollector": {"status": "enabled", "frequency": 35, "eps": 25}
            }, "active")
        agents_list = self.addAgent(agents_list, new_agent)
        if agentN is None:
            for agent in agents_list:
                self.printAgent(agent)
            self.writeAgent(agents_list, 'output.json')
        else:
            if agentN in range(MIN_RANGE_AGENT, MAX_RANGE_AGENT + 1):
                self.printAgent(agents_list[agentN - 1])
                self.writeAgent(agents_list[agentN - 1], 'output.json')
            else:
                print(f'Agent {agentN} does not exist')
        return


    '''
    Read json file with the agents list
    param data_file     filename
    return list of read element
    '''
    def loadAgent(self, data_file): 
        with open(Path(data_file)) as json_file:
            data = json.load(json_file)
        return data

    '''
    Write an agent or an agents list to a file
    param data          agent or agent list to be printed
    param data_file     filename  
    '''
    def writeAgent(self, data, data_file):
        newList = []
        file = open(data_file, 'w')
        if hasattr(data, '__iter__'):
            for agent in data:
                newList.append(self.jsonObjAux(agent))
            file.write(json.dumps(newList, indent=4, sort_keys=False))
        else:            
            file.write(json.dumps(self.jsonObjAux(data), indent=4, sort_keys=False))
        file.close()
        
    '''
    Auxiliary function to create a json variable
    param agent     agent info
    '''
    def jsonObjAux(self, agent:Agent):
        data_json = {"id": agent.getId(), 
                "name": agent.getName(), 
                "version": agent.getVersion(),
                "os": agent.getOs(), 
                "inventory": agent.getInventory(), 
                "modules": agent.getModules(),
                "status": agent.getStatus()}
        return data_json

    '''
    Print agent information
    param data      agent's data to be printed
    '''          
    def printAgent(self, data:Agent):
        data.showAttr()

    '''
    Add an agent to the agents list
    param data          agents list
    param new_agent     new agent to be added
    '''
    def addAgent(self, data, new_agent):
        data.append(new_agent)
        return data

'''
Entry point to solve Task 3
runScript can have argument or not
If no arguments output will be the list of agent
If argument in between MAX_RANGE_AGENT and MIN_RANGE_AGENT output will be agent information 
In argument is out of range message Agent does not exist
'''
if __name__ == '__main__':
    script = Script()
    script.runScript()