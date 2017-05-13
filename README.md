# python-graph-gui

Author: Sharif Shaker

Date of Creation: 5/8/2017

DISCRIPTION: Graph GUI project for creating graphs and running graph algorithms.

BASIC INFO: 
This project is designed for creating a graphical representation of a weighted graph with nodes and edges.  Graph algorithms can also be 
run on the graph and the results of the algorithms are displayed graphically.  

To use the full application run the GraphGuiApplication.py file.  

FILES:
The python files contained in the PythonGraphGui folder contain classes and functions for creating the graphical representation of graph and supporting user interaction with the graph.  

The internal PyGraph folder contains an underlying SGraph file and graph_path_algotithm file witch contain much of the basic logic for 
dealing with graphs.

  SGraph--
    contains a Graph class to represent a graph.  Uses a node dictionary and an edge dictionary to keep track of nodes and edges and 
    connections.  Also contains a function to print an adjacency list and functions to determine if graph is connected.  Graph class 
    supports both graphs and digraphs.
  
  graph_path_algorithms--
    contains various functions for running algorithms on input graphs and returning results of algorithm.
    Currently supports implementations of Dijkstra's, bellman ford's shortest path, and Prim's minimum spanning tree.
      
The GUI files utilize an underlying Graph object.  The underlaying graph can then be used with functions from the graph_path_algorithms 
to return results which are then taken and displayed graphically by the GUI objects.  
      
