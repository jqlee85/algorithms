# 1. Increase memory for your process in terminal: -ulimit s 32767 (limit holds only for the current session, if you restart terminal you will have to do it again)

import sys, threading, unittest
sys.setrecursionlimit(800000)
threading.stack_size(67108864)

def main():
    '''
    YOUR CODE HERE
    '''
    # Run Tests
    suite = unittest.TestLoader().loadTestsFromModule (TestMinCut())
    unittest.TextTestRunner().run(suite)

    # computeSCCs(None)

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
    ## Let f(v) = "finishing time" or each v in V

    #3 Run DFS Loop on G - Goal: Discover the SCCs one by one 
    ## Processing nodes in decreasing order of finishing times
    ## SCCs equal nodes with the same "leader" 


    
    
    return None

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

    
class TestMinCut(unittest.TestCase):
  
    def runTest(self):
        testGetGraph (self)

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
