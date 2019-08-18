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
import copy

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
        minCuts = None
    
    # Convert to ints
    for i in range(0,len(graph)):
        row = graph[i]
        for j in range(0,len(row)):
            graph[i][j] = int(graph[i][j])
 
    return graph

"""
Runs the randomContraction algorithm on an undirected graph n^2 times and returns the minimum number of cuts found

Args:
    graph: (list) An undirected graph representation consisting of V (a list of vertices) and E (a list of edges) ex: {vertices: [1,2,3,4], edges: [[1,2],[1,4],[2,3],[3,4]]}
    numIterations: (int) The number of times to run the random contraction algorithm before returning the min cut

Returns:
    minCuts: (int) the minimum number of cuts found through all the iterations of the randomContraction algorithm

"""
def getMinCut(graph,numIterations=100):
    minCuts = 'init'
    i = 0
    while (i < numIterations):
        seed = i+4
        graphCopy = copy.deepcopy(graph)
        finalGraph = randomContraction(graphCopy,seed)
        numCuts = getNumCrossing(finalGraph)
        if (numCuts < minCuts or minCuts == 'init'):
            minCuts = numCuts
        i += 1
    return minCuts    

"""
Performs a uniformly random contraction algorithm to get a final cut represented by 2 vertices

Args:
    graph: (list) An undirected graph representation, a list of lists, with the first element of each being the vertex, and the subsequent elements being references to the vertexes to which the vertex is connected
    seed: (int) The random seed used for selecting edges to collapse

Returns:
    finalCut: (list) of the final 2 vertices, ex: [1,3]

"""
def randomContraction(graph,seed=0):
    if (len(graph) == 2): # base case
        return graph
    else: # remove random edge and collapse
        return randomContraction(collapseRandomEdge(graph,seed),seed)
    
"""
Selects a random edge from a graph, and collapses the two nodes into one remaining node

Args:
    oldGraph: (list) An undirected graph representation, a list of lists, with the first element of each being the vertex, and the subsequent elements being references to the vertexes to which the vertex is connected
    seed: (int) The random seed used for selecting edges to collapse
    forceValues: (list) A list of two ints to be used to override random values when selecting and edge (only used for testing)

Returns:
    graph: (list) The resulting graph after the edge has been collapsed

"""
def collapseRandomEdge(graph,seed=0,forceValues=False):
    
    # Get random edge by randomly selecting a nodes, then randomly selecting a connected nodes from that list
    # Note: This isn't actually uniformly random, bc when picking the first node, a node with 1 edge is just as likely to be selected as a node with many edges
    # Thus, some edges are more likely than others to be selected by this method
    # TODO: Fix this to utilize weighted sampling of the first node
    random.seed(seed)
    
    # Node A
    nodeAIndex = random.randrange(0,len(graph))
    # Force Values (for testing)
    if (forceValues):
        nodeAIndex = forceValues[0]
    vertexA = graph[nodeAIndex][0]
    
    # Node B
    randomNodeIndexB = random.randrange(1,len(graph[nodeAIndex]))
    # Force Values (for testing)
    if (forceValues):
         randomNodeIndexB = forceValues[1]
    vertexB = graph[nodeAIndex][randomNodeIndexB]
    nodeBIndex = getNodeIndex(graph,vertexB)
    nodeB = graph[nodeBIndex] 

    #----- BEGIN Fuse A and B into single node by removing B -----#
    removedNode = graph.pop(nodeBIndex)
   
    newNodeAIndex = getNodeIndex(graph,vertexA)
    nodeA = graph[newNodeAIndex]

    # Remove reference to deleted node in nodeA
    if (vertexB in nodeA):
        while vertexB in nodeA: nodeA.remove(vertexB)
    
    # Loop through edges in removedNode and add to nodeA, while changing references in the connected nodes (nodeC) to point to nodeA
    i = 1
    while i < len(removedNode):
        # Get other end of edge from removed node
        vertexC = removedNode[i]
        if (vertexC != vertexA):
            nodeC = graph[getNodeIndex(graph,vertexC)]
            # Remove reference to deleted node in nodeC
            if (vertexB in nodeC):
                while vertexB in nodeC: nodeC.remove(vertexB)
            # Add vertex to nodeA
            nodeA.append(vertexC)
            # Add reference to remaining node in nodeC 
            nodeC.append(vertexA)
        i += 1       
     #----- /END Fuse two nodes into single node -----#
    return graph

"""
Gets index of the given vertex given in the graph adjacency list representation

Args:
    graph: (list) the list of lists representing the adjacency list of the graph

Returns:
    index: (int) The index of the list whose first value is the vertex

"""
def getNodeIndex(graph,vertexToFind):
    for i in range(0,len(graph)):
        if (graph[i][0] == vertexToFind):
            return i
    return False

"""
Performs a uniformly random contraction algorithm to get a final cut represented by 2 vertices

Args:
    collapsedGraph: (list) An undirected graph representation of a collapsed graph with two nodes

Returns:
    (int) The number of crossing edges of a 2 node graph

"""
def getNumCrossing(collapsedGraph):
    # print ('=>',collapsedGraph)
    return len(collapsedGraph[0]) - 1


"""
Performs a uniformly random contraction algorithm to get a final cut represented by 2 vertices

Args:
    collapsedGraph: (list) An undirected graph representation of a collapsed graph with two nodes

Returns:
    (int) The number of crossing edges of a 2 node graph

"""
class TestMinCut(unittest.TestCase):
  
    def runTest(self):
        testGetGraph (self)
        testGetNodeIndex (self)

    def testGetNumCrossing(self):
        graphInput = [
            [1,2,3,4,5,6],
            [6,1,2,3,4,5]
        ]
        self.assertEqual(getNumCrossing(graphInput),5)

    def testGetNodeIndex(self):
        graphInput = [
            [2,5,6],
            [1,4,6],
            [7,8],
            [10,2,6],
            [2,5,2]
        ]
        self.assertEqual(getNodeIndex(graphInput,7),2)
        self.assertEqual(getNodeIndex(graphInput,9),False)

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

    def testCollapseRandomEdge(self):
        initialGraph = [
            [1,2,3,4],
            [2,1,3,4],
            [3,1,2,4],
            [4,1,2,3,5],
            [5,4,6,7,8],
            [6,5,7,8],
            [7,5,6,8],
            [8,5,6,7]
        ]
        expectedGraph = [
            [1,2,3,5],
            [2,1,3,5],
            [3,1,2,5],
            [5,6,7,8,1,2,3],
            [6,5,7,8],
            [7,5,6,8],
            [8,5,6,7]
        ]
        forceValues = [4,1]
        self.assertEqual(collapseRandomEdge(initialGraph,0,forceValues),expectedGraph)
        
# Run Tests
suite = unittest.TestLoader().loadTestsFromModule (TestMinCut())
unittest.TextTestRunner().run(suite)

# Test Case 1
# adjacencyList = getGraph('./ex4testcases/ex4test1.txt')
# minCut = getMinCut(adjacencyList)
# print('MINIMUM CUT =>'+str(minCut))

# Test Case 2
# graph = getGraph('./ex4testcases/ex4test_16_50.txt')
# minCut = getMinCut(graph)
# print('MINIMUM CUT =>'+str(minCut))

# Assignment Input
graph = getGraph('./ex4input.txt')
minCut = getMinCut(graph)
print('MINIMUM CUT =>'+str(minCut))
