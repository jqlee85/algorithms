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
def randomContraction(graph,seed=0):

    if (len(graph) == 2): # base case
        return [getNumCrossing(graph),[graph[0][0],graph[1][0]]]
    else: # remove random edge and collapse
        newGraph = collapseRandomEdge(graph,seed)
        return randomContraction(newGraph,seed)
    

def getNumCrossing(graph):
    return len(graph[0])

def collapseRandomEdge(graph,seed):
    random.seed(seed)
    randomNodeIndexA = random.randrange(0,len(graph),seed)
    randomNodeIndexB = random.randRange(0,len(graph[randomNodeIndexA]),seed)
    nodeB = graph[randomNodeIndexB] 
    nodeBIndex = getNodeBIndex(graph)
    removedNode = graph.pop(nodeBIndex)

    if (nodeBIndex < randomNodeIndexA):
        randomNodeIndexA -= 1
    
    i = 1
    while i <= len(removedNode):
        if (removedNode[i] not in graph[randomNodeIndexA]):
            graph[randomNodeIndexA].push(removedNode[i])
            # TODO find row of removedNode[i] and add randomNodeIndexA to it if not already there

    return graph

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
    
"""
Takes a text file of an adjacency list in columns and returns an undirected graph representation consisting of V (a list of vertices) and E (a list of edges) ex: {vertices: [1,2,3,4], edges: [[1,2],[1,4],[2,3],[3,4]]}

Args:
    graph: (string) The location of the .txt file containing the adjacency list

Returns:
    graph: (list) The graph representation

"""
def getGraph(adjacencyListLocation):

    # Read in data from txt file
    text_file = open(adjacencyListLocation, "rt")
    graph = [[item for item in line.split()] for line in text_file.readlines()]
    
    # Check for initial row with expected minCuts
    if (graph[0][0] == '#'):
        graph.pop(0)
    else:
        minCuts = null
    
    # Convert to ints
    i = 0
    while i < len(graph):
        row = graph[i]
        j = 0
        while j < len(row):
            graph[i][j] = int(graph[i][j])
            j += 1
        i += 1
 
    return graph

# graph = getGraphFromAdjacencyList('./ex4testcases/ex4test1.txt')
# print(graph)

class TestMinCut(unittest.TestCase):
  
    def runTest(self):
        testGetGraph (self)

    def getNumCrossing(self)
        expectedNum = 3
        

    def testGetGraph(self):
        expectedGraph = [
            [1,2,3,4],
            [2,1,3,4],
            [3,1,2,4],
            [4,1,2,3,5],
            [5,4,6,7,8],
            [6,5,7,8],
            [7,5,6,8],
            [8,5,6,7]
        ]
        expectedMinCuts = 1
        self.assertEqual(getGraph('./ex4testcases/ex4test1.txt'),expectedGraph)

# theTest = TestMinCut()
# theTest.test()

suite = unittest.TestLoader().loadTestsFromModule (TestMinCut())
unittest.TextTestRunner().run(suite)


