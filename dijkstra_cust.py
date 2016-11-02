# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 12:16:08 2016

@author: Baptiste
"""

import pandas as pd

# set working directory
# cd /Users/Baptiste/Documents/WORK/COLUMBIA/3. Fall 2016/IEOR4418 - Transportation Data Analytics

# Passenger Class
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

# customized Dijkstra Algorithm with specified origin a and maximum number of steps k
def dijkstra_cust_origin(graph,a,k):
    # Dijkstra algorithm starting from origin a in k steps

    # 0. initialization
    global explored_nodes
    global unexplored_nodes
    global all_nodes    
    explored_nodes = []
    unexplored_nodes = []
    all_nodes = []
    count = 0
    
    for i in range(1,len(graph)+1):
        exec("node%d = Node(i)" % (i));
        exec("all_nodes.append(node%d)" % i);
        exec("unexplored_nodes.append(node%d)" % i);
    
    all_nodes[a-1].distance = 0
    all_nodes[a-1].pred = a
    all_nodes[a-1].path = str(a)
        
    while (set(explored_nodes) != set(all_nodes) and count <= k):        
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
        count += 1
                    
    # 3. summarize
    print("")
    print("Shortest Path from origin "+str(all_nodes[a-1].node_number)+" to sink "+str(all_nodes[-1].node_number)+": "+all_nodes[-1].path)
    print("Shortest Path Weight: "+str(all_nodes[-1].distance))
    print("")
    print("Detailed Summary:")
    summary(graph)            


graph1 = pd.read_csv("graph1.csv")
graph2 = pd.read_csv("graph2.csv")

dijkstra_cust_origin(graph2,1,3)

