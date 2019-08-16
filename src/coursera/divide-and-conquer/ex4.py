# The file contains the adjacency list representation of a simple undirected graph. 
# There are 200 vertices labeled 1 to 200. 
# The first column in the file represents the vertex label, and the particular row (other entries except the first column) tells all the vertices that the vertex is adjacent to. 
# So for example, the 6^{th} row looks like : "6	155	56	52	120	......". 
# This just means that the vertex with label 6 is adjacent to (i.e., shares an edge with) the vertices with labels 155,56,52,120,......,etc

# Your task is to code up and run the randomized contraction algorithm for the min cut problem and use it on the above graph to compute the min cut. 
# (HINT: Note that you'll have to figure out an implementation of edge contractions. 
# Initially, you might want to do this naively, creating a new graph from the old every time there's an edge contraction. 
# But you should also think about more efficient implementations.) 
# (WARNING: As per the video lectures, please make sure to run the algorithm many times with different random seeds, and remember the smallest cut that you ever find.) 
# Write your numeric answer in the space provided. So e.g., if your answer is 5, just type 5 in the space provided.

import unittest
import random
import sys

"""
Performs a uniformly random contraction algorithm to get a final cut represented by 2 vertices

Args:
    graph: (list) An undirected graph representation consisting of V (a list of vertices) and E (a list of edges) ex: {vertices: [1,2,3,4], edges: [[1,2],[1,4],[2,3],[3,4]]}
    randomSeed: (int) The random seed used for selecting edges to collapse

Returns:
    finalCut: (list) of the final 2 vertices, ex: [1,3]

"""
def randomContraction(graph):

    finalCut = null
    return finalCut


"""
Runs the randomContraction algorithm on an undirected graph n^2 times and returns the minimum number of cuts found

Args:
    graph: (list) An undirected graph representation consisting of V (a list of vertices) and E (a list of edges) ex: {vertices: [1,2,3,4], edges: [[1,2],[1,4],[2,3],[3,4]]}

Returns:
    minCuts: (int) the minimum number of cuts found through all the iterations of the randomContraction algorithm

"""
def getMinCut(graph):

    n = len(graph.vertices)
    m = len(graph.edges)
    numIterations = n ** 2
    minCuts = m
    minCut = null

    i = 1
    while (i <= numIterations):
        [numCuts,finalCut] = randomContraction(graph,i)
        if (numCuts < m):
            minCuts = numCuts
            minCut = finalCut
        i += 1

    return minCuts    
    


