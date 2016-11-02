# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 12:16:08 2016

@author: Baptiste
"""

import pandas as pd

# cd /Users/Baptiste/Documents/WORK/COLUMBIA/3. Fall 2016/IEOR4418 - Transportation Data Analytics
# pwd

#Passenger Class
class Node:
    number_of_nodes = 0
    
    def __init__(self,node_number):
        self.node_number = node_number
        self.__distance = 10000
        self.__pred = 0
        self.__path = ""
        
    @property 
    def distance(self):
        return self.__distance
        
    @property 
    def pred(self):
        return self.__pred

    @property 
    def path(self):
        return self.__path

def info_node(node):
    print("Node " + str(node.node_number) + " - Distance to orignin: " + str(node.distance) + " - Pred: " + str(node.pred) + " - Path: " + node.path)

def summary(graph):
    for i in range(0,len(graph)):
        info_node(all_nodes[i])

def dijkstra(graph):
    # Classic Dijkstra algorithm

    # 0. initialization
    global explored_nodes
    global unexplored_nodes
    global all_nodes
    explored_nodes = []
    unexplored_nodes = []    
    all_nodes = []
    
    for i in range(1,len(graph)+1):
        exec("node%d = Node(i)" % (i));
        exec("all_nodes.append(node%d)" % i);
        exec("unexplored_nodes.append(node%d)" % i);
    
    node1.distance = 0
    node1.pred = 1
    node1.path = "1"
        
    while (set(explored_nodes) != set(all_nodes)):        
    # 1. find the minimum distance unprocessed node
        min_unprocessed_distance = 10000
        min_unprocessed_node = 0
        ind = -1
        for i in range(0,len(unexplored_nodes)):
            if (unexplored_nodes[i].distance < min_unprocessed_distance):
                min_unprocessed_distance = unexplored_nodes[i].distance
                min_unprocessed_node = unexplored_nodes[i]
                ind = i
                #print('--> the minimum unprocessed node is node number '+ str(min_unprocessed_node.node_number)+' with distance to origin '+str(min_unprocessed_node.distance))
        explored_nodes.append(unexplored_nodes.pop(ind))
        
    # 2. process other nodes from this node
        for i in range(0,len(unexplored_nodes)):
            for j in range(0,len(explored_nodes)):
                if (unexplored_nodes[i].distance > min_unprocessed_node.distance + graph[str(unexplored_nodes[i].node_number)][min_unprocessed_node.node_number-1]):
                    unexplored_nodes[i].distance = min_unprocessed_node.distance + graph[str(unexplored_nodes[i].node_number)][min_unprocessed_node.node_number-1]
                    unexplored_nodes[i].pred = min_unprocessed_node.node_number
                    unexplored_nodes[i].path = (min_unprocessed_node.path + ' > ' + str(unexplored_nodes[i].node_number))
                    
    # 3. summarize
    print("")
    print("Shortest Path from origin "+str(all_nodes[0].node_number)+" to sink "+str(all_nodes[-1].node_number)+": "+all_nodes[-1].path)
    print("Shortest Path Weight: "+str(all_nodes[-1].distance))
    print("")
    print("Detailed Summary:")
    summary(graph) 
    
    
# run Dijkstra Algorithm on two instances (see csv files in directory)
graph1 = pd.read_csv("dijkstra_example.csv")
graph2 = pd.read_csv("C.csv")

dijkstra(graph1)
dijkstra(graph2)
