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

    print ('G.nodes',G.nodes)
    print ('G.reverseNodes',G.reverseNodes)
    
    #1 Reverse G to get Grev

    #2 Run DFS Loop on GRev - Goal: to compute magical ordering of nodes
    ## Let f(v) = "finishing time" for each v in V
    DFSLoop1(G)

    #3 Run DFS Loop on G - Goal: Discover the SCCs one by one 
    ## Processing nodes in decreasing order of finishing times
    DFSLoop2(G)
    
    ## SCCs equal nodes with the same "leader" 
    print G.leaders

    return None

# First dfs loop performed on reversed graph
def DFSLoop1(G):
    G.reverseGraph()
    
    # Loop from n down to 1
    for i in reversed(range(1,G.numNodes+1)):
        
        if (not G.isExplored(i)):
            G.setCurrentSource(i)
            # Call DFS 
            DFS(G,i)

    print('G.finishingTimes',G.finishingTimes)

# Second dfs loop performed on forward graph
def DFSLoop2(G):
    G.unReverseGraph()
    
    # Loop from n down to 1
    for i in reversed(range(1,G.numNodes+1)):
        nodeId = G.finishingTimes[i-1]
        if (not G.isExplored(nodeId)):
            G.setCurrentSource(nodeId)
            # Call DFS 
            DFS(G,nodeId)

    print('G.finishingTimes',G.finishingTimes)
    
# Depth First Search
def DFS(G,i):
    node = G.getNode(i)
    G.setExplored(i)
    G.setLeader(i,G.currentSource)
    #for each arc (i,j) in G
    outgoingEdges = G.getOutgoingEdges(i)
    for j in range(0,len(outgoingEdges)):
        nextNode = outgoingEdges[j]
        # if next node not yet explored
        if ( not G.isExplored(nextNode)):
            print('j not explored, call DFS',nextNode)
            DFS(G,nextNode)
    G.incNumNodesProcessed()
    print('setFinish for '+str(i)+' to '+str(G.numNodesProcessed))
    G.setFinishingTime(i,G.numNodesProcessed)
 



"""
Graph Class 

Args:
    graph: (string) The location of the .txt file containing list of edges

"""
# Graph Class, takes in list of edges, and converts to an adjacency list
class Graph:

    edges = None
    nodes = None # Adjacency list
    reverseNodes = None
    numNodes = 0
    numEdges = 0
    numNodesProcessed = 0
    reverse = False
    explored = None
    leaders = None
    finishingTimes = None
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
        self.reverseNodes = [[x+1] for x in range(0,numNodes)]
        self.leaders = [[] for x in range(0,numNodes)]
        self.explored = [False for x in range(0,numNodes)]
        self.finishingTimes = [[] for x in range(0,numNodes)]
        self.finishingTimeIndex = [[] for x in range(0,numNodes)]


        # Populate adj list
        for i in self.edges:
            # Forward List
            if (i[1] not in self.nodes[i[0]-1]):
                self.nodes[i[0]-1].append(i[1])
            # if (i[0] not in self.nodes[i[1]-1]):
                # self.nodes[i[1]-1].append(i[0])
            # Reverse List
            if (i[0] not in self.reverseNodes[i[1]-1]):
                self.reverseNodes[i[1]-1].append(i[0])
            # if (i[1] not in self.reverseNodes[i[1]-1]):
                # self.reverseNodes[i[1]-1].append(i[1])   
    # END __init__
    
    def getNode(self,nodeId):
        if self.reverse: return self.reverseNodes[nodeId-1]
        else: return self.nodes[nodeId-1]

    def getLeader(self,nodeId):
        return self.leaders[nodeId - 1]

    def setLeader(self,nodeId,leaderNodeId):
        self.leaders[nodeId-1] = leaderNodeId

    def resetLeaders(self):
        self.leaders = [None for x in range(0,self.numNodes)]

    def isExplored(self,nodeId):
        return self.explored[nodeId - 1]

    def setExplored(self,nodeId):
        self.explored[nodeId-1] = True
    
    def resetExplored(self):
        self.explored = [False for x in range(0,self.numNodes)]

    def getFinishingTime(self,nodeId):
        return self.finishingTimes[nodeId - 1]

    def setFinishingTime(self,nodeId,finishingTime):
        self.finishingTimes[nodeId-1] = finishingTime
        self.finishingTimeIndex[finishingTime-1] = nodeId

    def getNodeByFinishTime(self,finishingTime):
        nodeId = self.finishingTimeIndex[finishingTime-1]
        return self.getNode(nodeId)

    def resetFinishingTimes(self):
        self.finishingTimes = [None for x in range(0,self.numNodes)]  

    def setCurrentSource(self,nodeId):
        self.currentSource = nodeId

    def resetCurrentSource(self):
        self.currentSource = None
    
    def incNumNodesProcessed(self):
        self.numNodesProcessed += 1

    def resetNumNodesProcessed(self):
        self.numNodesProcessed = 0
    
    def reverseGraph(self,):
        self.reverse = True

    def unReverseGraph(self):
        self.reverse = False

    def getOutgoingEdges(self,nodeId):
        return self.getNode(nodeId)[1:]
    

class TestMinCut(unittest.TestCase):
  
    def runTest(self):
        testGetGraph (self)
        testGetNumNodes (self)

    def testGetGraph(self):
        adjacencyList = [[1, 12, 3], [2, 3, 13], [3, 2, 1], [4], [5, 7, 14], [6], [7, 5, 10], [8, 16, 12], [9], [10, 7, 15], [11, 14, 16], [12, 1, 8], [13, 2, 15], [14, 11, 5], [15, 10, 13], [16, 8, 11]]
        G = Graph('./ex1testdata/input_mostlyCycles_8_16.txt')
    
        self.assertEqual(G.nodes,adjacencyList)

        G.setFinishingTime(2,5)
        G.setFinishingTime(1,9)
        G.setFinishingTime(10,4)
        self.assertEqual(G.getNodeByFinishTime(5),[2,3,13])
        self.assertEqual(G.getFinishingTime(10),4)
        
        G.setExplored(4)
        self.assertEqual(G.isExplored(4),True)
        self.assertEqual(G.isExplored(3),False)
        G.resetExplored()
        self.assertEqual(G.isExplored(4),False)
        
thread = threading.Thread(target=main)
thread.start()
