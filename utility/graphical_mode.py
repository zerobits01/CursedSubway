import networkx as nx
import matplotlib.pyplot as plt
from classes.subway import SubwayLine

# Defining a Class 
class GraphVisualization:
    def __init__(self): 
        self.visual = [] 

    def addEdge(self, a, b): 
        temp = [a, b] 
        self.visual.append(temp) 
          
    def visualize(self): 
        G = nx.Graph() 
        G.add_edges_from(self.visual) 
        nx.draw_networkx(G) 
        plt.show() 


def visualize_subway_lines(lines):
    if type(lines) is not list or len(lines) == 0:
        raise ValueError("lines should be a non empty list of subway lines")
    for line in lines:
        if not issubclass(type(line), SubwayLine):
            raise ValueError("each line in subway lines should be type of SubwayLine Class")
    G = GraphVisualization()
    for line in lines:
        stations = line.stations
        len_stat = len(stations) - 1
        for i in range(0,len_stat):
            G.addEdge(stations[i].name, stations[i+1].name)
    G.visualize()
# Driver code # this is only for test to know the action of networkx
'''
G = GraphVisualization()
G.addEdge("Tajrish", "shariati") # later i can add these to subway lines!
G.addEdge("shariati", "beheshti")
G.addEdge("beheshti", "dolat")
G.addEdge("dolat", "mohammadie")
G.addEdge("mohammadie", "kaharizak")
G.addEdge("sanaat", "valiasr")
G.addEdge("valiasr", "teatr")
G.addEdge("teatr", "mohammadie")
G.addEdge("mohammadie", "molavi")
G.addEdge("molavi", "basij")
G.addEdge("satari", "valiasr")
G.addEdge("valiasr", "jahad")
G.addEdge("jahad", "beheshti")
G.addEdge("beheshti", "heravi")
G.addEdge("heravi", "ghaem")
G.addEdge("azadi", "teatr")
G.addEdge("teatr", "ferdowsi")
G.addEdge("ferdowsi", "dolat")
G.addEdge("dolat", "shemiran")
G.addEdge("shemiran", "bouali")
G.visualize()
'''