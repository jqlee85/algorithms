# 1. Increase memory for your process in terminal: ulimit -s 65532 (limit holds only for the current session, if you restart terminal you will have to do it again)

import sys, threading, unittest
sys.setrecursionlimit(4000000)
threading.stack_size(67108864)

def main():

    # Get path to graph to compute from user input or default
    graphPath = sys.argv[1] if len(sys.argv) > 1 and sys.argv[1] else './ex1input.txt'
    
    # Run Tests
    suite = unittest.TestLoader().loadTestsFromModule (TestMinCut())
    unittest.TextTestRunner().run(suite)

    # Get Graph
    G = Graph(graphPath)

    print(G.nodes)
    print(G.explored)
    # Compute SCCs
    return computeSCCs(G)

"""
Takes a graph represented as an list of directed edges, ie: [[1,2],[1,3],[2,4],[3,4]] and computes the n largest SCCs and returns their sizes in descending order

Args:
    G: (list) The list representation of the graph
    numSCCs: (int) The number of the largest SCCs to return. 

Returns:
    largestSCCSizes: (list) The sizes of the largest SCCs in descending order

"""
def computeSCCs(G,numSCCs=5):

    
    #1 Reverse G to get Grev

    #2 Run DFS Loop on GRev - Goal: to compute magical ordering of nodes
    ## Let f(v) = "finishing time" for each v in V
    n = G.numNodes
    # DFSLoop1(G,n)

    #3 Run DFS Loop on G - Goal: Discover the SCCs one by one 
    ## Processing nodes in decreasing order of finishing times
    ## SCCs equal nodes with the same "leader" 

    return None

# First dfs loop performed on reversed graph
def DFSLoop1(G,n):

    t = 0 # num of nodes processed so far
    s = [None] #current source vertex, should be 1 indexed
    
    explored = [None] * n # OBO (0 indexed)
    leaders = [None] * n # Values refer to node labels (1 indexed)
    finishingTimes = [None] * n
    
    for i in reversed(range(1,n+1)):
        
        if (not explored[i-1]):
            s[0] = i # source vertex (value refers to node labels, 1 indexed)
            # Call DFS 
            DFS(G,i,explored,leaders,finishingTimes,s)

    print('Explored',explored)
    print('leaders',leaders)
    print('finishingTimes',finishingTimes)
    
# Depth First Search
def DFS(G,i,explored,leaders,finishingTimes,s):
    node = G[i]
    explored[i] = True
    leaders[i] = s[0]
    #for each arc (i,j) in G
    for arc in G:
        j = arc[1]
        print('check',j)
        print('explored',explored)
        # if j not yet explored
        if ( not explored[j-1]):
            print('j not explored, call DFS',j)
            DFS(G,j,explored,leaders,finishingTimes,s)

    t += 1
    finishingTimes[i-1] = t
 



"""
Takes a text file list of edges and converts it to an array

Args:
    graph: (string) The location of the .txt file containing edges

Returns:
    graph: (list) The graph representation

"""
def getGraph(listLocation):

    # Read in data from txt file
    text_file = open(listLocation, "rt")
    graph = [[item for item in line.split()] for line in text_file.readlines()]
    
    # Convert to ints
    for i in range(0,len(graph)):
        row = graph[i]
        for j in range(0,len(row)):
            graph[i][j] = int(graph[i][j])
 
    return graph

# Graph Class, takes in list of edges, and converts to an adjacency list
class Graph:

    edges = None
    nodes = None # Adjacency list
    numNodes = 0
    numEdges = 0
    reverse = False
    explored = None
    leaders = None
    currentSource = None

    def __init__(self, listLocation):
        
        # Read in data from txt file
        text_file = open(listLocation, "rt")
        edgesList = [[item for item in line.split()] for line in text_file.readlines()]
        
        # Convert to ints
        for i in range(0,len(edgesList)):
            row = edgesList[i]
            for j in range(0,len(row)):
                edgesList[i][j] = int(edgesList[i][j])

        self.edges = edgesList
        self.numEdges = len(edgesList)
        # Get number of nodes in graph
        numNodes = 0
        
        # Loop through all edges
        for edge in edgesList:
            # Check for larger node number
            if (edge[0] > numNodes): 
                numNodes = edge[0]
            elif (edge[1] > numNodes): 
                numNodes = edge[1]
        
        # Set numNodes largest node number
        self.numNodes = numNodes
        
        # Initialize adjacency list
        self.nodes = [[x+1] for x in range(0,numNodes)]
        self.leaders = [[] for x in range(0,numNodes)]
        self.explored = [[] for x in range(0,numNodes)]


        # Populate adj list
        for i in self.edges:
            if (i[1] not in self.nodes[i[0]-1]):
                self.nodes[i[0]-1].append(i[1])
            if (i[0] not in self.nodes[i[1]-1]):
                self.nodes[i[1]-1].append(i[0])
             

    def getLeader(nodeNumber):
        return self.leaders[nodeNumber - 1]

    def setLeader(nodeNumber):
        self.leaders[nodeNumber-1] - nodeNumber

    def isExplored(nodeNumber):
        return self.explored[nodeNumber - 1]

    def setExplored(nodeNumber):
        self.explored[nodeNumber-1] = True

    def setCurrentNode(nodeNumber):
        self.currentSource = nodeNumber

    def reverseGraph():
        self.reverse = True
        print('not implemented reverseGraph')

    def unReverseGraph():
        self.reverse = False
        print('not implemented unReverseGraph')
    
    def resetExplored():
        self.explored = [[] for x in range(0,self.numNodes)]

    def resetLeaders():
        self.leaders = [[] for x in range(0,self.numNodes)]
            
    def resetCurrentSource():
        self.currentSource = None
    
    

class TestMinCut(unittest.TestCase):
  
    def runTest(self):
        testGetGraph (self)
        testGetNumNodes (self)

    def testGetGraph(self):
        expectedGraph = [
            [1,12],
            [2,3],
            [3,1],
            [5,7],
            [7,10],
            [8,16],
            [10,15],
            [11,14],
            [12,8],
            [13,2],
            [14,5],
            [15,13],
            [16,11]
        ]
        self.assertEqual(getGraph('./ex1testdata/input_mostlyCycles_8_16.txt'),expectedGraph)
        
thread = threading.Thread(target=main)
thread.start()
