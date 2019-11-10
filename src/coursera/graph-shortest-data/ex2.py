# The file contains an adjacency list representation of an undirected weighted graph with 200 vertices labeled 1 to 200. Each row consists of the node tuples that are adjacent to that particular vertex along with the length of that edge. For example, the 6th row has 6 as the first entry indicating that this row corresponds to the vertex labeled 6. The next entry of this row "141,8200" indicates that there is an edge between vertex 6 and vertex 141 that has length 8200. The rest of the pairs of this row indicate the other vertices adjacent to vertex 6 and the lengths of the corresponding edges.

# Your task is to run Dijkstra's shortest-path algorithm on this graph, using 1 (the first vertex) as the source vertex, and to compute the shortest-path distances between 1 and every other vertex of the graph. If there is no path between a vertex v and vertex 1, we'll define the shortest-path distance between 1 and v to be 1000000. 

# You should report the shortest-path distances to the following ten vertices, in order: 7,37,59,82,99,115,133,165,188,197. You should encode the distances as a comma-separated string of integers. So if you find that all ten of these vertices except 115 are at distance 1000 away from vertex 1 and 115 is 2000 distance away, then your answer should be 1000,1000,1000,1000,1000,2000,1000,1000,1000,1000. Remember the order of reporting DOES MATTER, and the string should be in the same order in which the above ten vertices are given.

import sys, unittest

def main():

    # Get path to graph to compute from user input or default
    graphPath = sys.argv[1] if len(sys.argv) > 1 and sys.argv[1] else './ex2input.txt'

    # Run Tests
    suite = unittest.TestLoader().loadTestsFromModule (TestShortestPath())
    unittest.TextTestRunner().run(suite)

    # Get Graph
    G = Graph(graphPath)

    # Calculate Shortest Paths
    shortestPaths = getShortestPaths(G)


def getShortestPaths(graph):

    print('getShortestPaths')

    # Initialize processed vertices
    X = [1]

    # Computed shortest path distances
    A = [0]

    # Computes shortest paths (optional)
    B = [[1]]

    # Create heap??? 

    # Main while loop
    # while(len(X) < graph.numNodes):

        # Among all edges (v,w) with v in X and head in V-X, pick the edge that minimizes A[v] + length(vw)
        # Call edge (v*,w*)
        # This should be pulling the minimum from the heap

        # Add w* to X

        # Set A[w*] to A[v*] + length(v*,w*)

        # Set B[w*] to B[v*] u(v*,w*)  [ adding the edge to the previous path]


# Graph Class, takes in list of edges, and converts to an adjacency list
class Graph:

    numNodes = 0
    

    def __init__(self, listLocation):
        
        # Read in data from txt file
        text_file = open(listLocation, "rt")
        adjList = [[item for item in line.split()] for line in text_file.readlines()]

        # Convert to ints
        for i in range(0,len(adjList)):
            row = adjList[i]
            adjList[i][0] = int(adjList[i][0])
            for j in range(1,len(row)):
                
                headNode =  int(adjList[i][j].split(',')[0])
                distance =  int(adjList[i][j].split(',')[1])
                adjList[i][j] = [headNode,distance]
                if (i == 1): 
                    print( adjList[i][j])
                    
        
        # Set numNodes largest node number
        self.numNodes = len(adjList)

        print(adjList)
        
    # END __init__


    
class TestShortestPath(unittest.TestCase):
  
    def runTest(self):
        testGetGraph (self)

    def testGetGraph(self):
       
        # Test graph parsing
        # G = Graph('./ex2testdata/classExample.txt')
        # self.assertEqual(G.nodes,[[1,4],[2,8],[3,6],[4,7],[5,2],[6,9],[7,1],[8,5,6],[9,3,7]])
        print('testGetGraph')

       
main()