# dijkstra_algorithms

This folder contains two versions of the well known Dijkstra Algorithm::

- dijkstra.py features the algorithm in its most classic version

- dijkstra_cust.py offers additional functionality: user can choose an origin a wherever he wants in the graph and get shortest path to any other nodes. This version also allows to limit the number of steps k in the algorithm (complete iterations)

Two csv files offer the possibility to test the algorithm on a practical dataset and see the results. These two files contain square matrices of integers. If we call our matrix A with aij elements of the square matrix:

- first line and columns represent the nodes

- aij gives the weight of the edge from the node in column j to the node in row i

- for all i, aii = 0 (diagonal elements are null since they represent the weight from a node to itself) This assumption can be changed if we assume the existence of delay in our nodes.

- when aij = 100, we assume the weight as infinite on this given arc. 100 is just an arbitrary value, it could have been 1,000,000 and it is just here for the algorithm to run well. In real life, this situation would corespond to a pair of nodes (i,j) where the nodes are not connected. 
