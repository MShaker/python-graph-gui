import sys
from queue import PriorityQueue
import heapq
import random

''' Graph Path Algortihm File
  
    Author: Sharif Shaker
    Date: 4/29/2017
    
    Modified: 5/5/2017 
    Changes made: added prims algorithm to find minimum spanning tree of an input graph

    Description:
        This file contains graph traversal and shortest path finding, and minimum spanning tree algorithms

'''

def dijkstra(graph, from_v, to_v_list=None):
  q = PriorityQueue() # create a priority queue
  node_dict = {}  # create a node dictionary to return a distance, parent pair given a node value 
  current = (None, None) # holds the currently selected node
  edge_w = None
	
  if to_v_list is None: to_v_list = node_dict.keys() # if no node was input, find path to all nodes

  # make start node is valid	
  if from_v not in graph.nodes_dict:
    print ('Invalid start node of ' + str(from_v))
    return
	  
  # make sure destination nodes are valid
  for node in to_v_list:
    if node not in graph.nodes_dict:
      print ('Invalid end node of ' + str(node))
      return	
    
  # set up algorithm start conditions
  for node in graph.nodes_dict.keys(): # for each node
    if node == from_v: # if node is the start node
      q.put((0, node))  # put node in queue with 0 distance
      node_dict[node] = (0, node) # put into dictionary with 0 distance and itself as a parent
    else:
      node_dict[node] = (float('inf'), None) # put all other nodes in dictionary with largest possible distance and no parent
		
  while not q.empty():
    current = q.get() # get node with shortest distance from start
    for adj_node in graph.nodes_dict[current[1]]: # for each adjacent node
      edge_w = graph.edges_dict[(current[1], adj_node)]
      if edge_w < 0: return [('Invalid', -1, None)]
      dist = current[0] + edge_w
      if dist < node_dict[adj_node][0]: # if distance to start is less than it originally was 
        q.put((dist, adj_node)) # put new dist parent pair in queue
        node_dict[adj_node] = (dist, current[1]) # change value in node dictionary
    
  result = []
  for node in to_v_list: # go through all end nodes 
    path = [node] 
    total_dist = node_dict[node][0] # set total distance to dist from start to goal node
    if total_dist == float('inf'): # if path wasn't found
      result.append((node, total_dist, None)) # return result with None 
    else:  
      while path[0] != from_v: # while node at 0 index is not start node
        path.insert(0, node_dict[path[0]][1]) # insert parent into 0 index of path
      result.append((node, total_dist, path)) # add path to result list
		  
  return result	  



def prims(graph):
  if not graph.is_connected(): return None # if graph is not connected return None
  nodes_list = [] 
  edges_list = [] 
  edges_q = PriorityQueue() 
  current = random.choice(list(graph.nodes_dict.keys())) # randomly select a node
  nodes_list.append(current) # add to list of nodes
  while len(nodes_list) < len(graph.nodes_dict): # while all nodes have not been added to list
    edges_q.queue.clear() # clear the queue
    for node in nodes_list: # for each node in list
      for adj_node in graph.nodes_dict[node]: # go through adjacent nodes
        weight = graph.edges_dict[(node, adj_node)] 
        if adj_node not in nodes_list: # if the adjacent node is not in the node list
          edges_q.put((weight, node, adj_node)) # add associated edge to queue
    min_edge = edges_q.get() # get the smallest weight edge from the queue
    edges_list.append(min_edge) # add the edge to edge list
    nodes_list.append(min_edge[2]) # add the associated node to node list

  return edges_list # return list of edges

      
          