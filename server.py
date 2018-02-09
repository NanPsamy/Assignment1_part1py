
from graph import Graph
import binary_heap

def least_cost_path(graph, start, dest, cost):
    """Find and return a least cost path in graph from start
    vertex to dest vertex.
    Efficiency: If E is the number of edges, the run-time is
    O( E log(E) ).
    Args:
    graph (Graph): The digraph defining the edges between the
    vertices.
    start: The vertex where the path starts. It is assumed
    that start is a vertex of graph.
    dest: The vertex where the path ends. It is assumed
    that dest is a vertex of graph.
    cost: A class with a method called "distance" that takes
    as input an edge (a pair of vertices) and returns the cost
    of the edge. For more details, see the CostDistance class
    description below.
    Returns:
    list: A potentially empty list (if no path can be found) of
    the vertices in the graph. If there was a path, the first
    vertex is always start, the last is always dest in the list.
    Any two consecutive vertices correspond to some
    edge in graph.

    """
    reached = {}  # start with an empty dictionary
    events = binary_heap.BinaryHeap()  # Create empty heap
    events.insert([start, start], 0)  # Vertex burns at time 0
    while len(events) > 0:
        edge, time = events.popmin()
        if edge[1] not in reached:
            reached[edge[1]] = edge[0]
            for neighbor in graph.neighbours(edge[1]):
                events.insert([edge[1], neighbor], time + cost.distance([edge[1], neighbor]))
    return reached




def load_edmonton_graph(filename):
    """
    Loads the graph of Edmonton from the given file.
    Returns two items
    graph: the instance of the class Graph() corresponding to the
    directed graph from edmonton-roads-2.0.1.txt
    location: a dictionary mapping the identifier of a vertex to
    the pair (lat, lon) of geographic coordinates for that vertex.
    These should be integers measuring the lat/lon in 100000-ths
    of a degree.
    In particular, the return statement in your code should be
    return graph, location
    (or whatever name you use for the variables).
    Note: the vertex identifiers should be converted to integers
    before being added to the graph and the dictionary.
    """
    #read from the file 'filename'
    with open(filename,'r') as inputFile:
        g = Graph()# new graph g to add nodes and edges in
        location= {}# new dictionary containing vertex and (lat,lon)
        #read all the files
        for line in inputFile:
            CSV_line = line.strip().split(',')# comma separate entries
            if CSV_line[0]=="V":#if V is the first part of the line
                g.add_vertex(int(CSV_line[1]))#add vertex
                #add coordinates to vertex in location (multiply lat,lon by 10^5)
                location[int(CSV_line[1])]=[int(float(CSV_line[2])*100000),int(float(CSV_line[3])*100000)]
            elif CSV_line[0]=="E":#if E is the first part of the line
                g.add_edge((int(CSV_line[1]),int(CSV_line[2])))#add edge on next inputs

    return g, location # return graph and location dictionary
    #Create edmonton graph based on txt file and print the edmonton graph's components

class CostDistance:
    """
    A class with a method called distance that will return the Euclidean
    between two given vertices.
    """
    def __init__(self, location):
        """
        Creates an instance of the CostDistance class and stores the
        dictionary "location" as a member of th is class.
        """
        self.location = location

    def distance(self, e):
        """
        Here e is a pair (u,v) of vertices.
        Returns the Euclidean distance between the two vertices u and v.
        """
        coord01, coord02 = e #first vertex and second vertex
        lat =0 #index of latidude of vertex
        lon = 1 #index of latidude of vertex
        # calculating the euclidean distance
        Euclidean= (((self.location[coord01][lat]-self.location[coord02][lat]))**2+(self.location[coord01][lon]-self.location[coord02][lon])**2)**(1/2.0)
        return Euclidean #return Euclidean distance


if __name__ =="__main__":
    edmonton_Graph, vertice_Locations = load_edmonton_graph('edmonton-roads-2.0.1.txt') # Load edmonton_Graph and locations dict
    costObject = CostDistance(vertice_Locations)

    test, lat01, lon01, lat02, lon02 = input().split()
    coord01L =[int(lat01),int(lon01)]
    coord02L = [int(lat02), int(lon02)]
    startpoint = None
    endpoint = None
    if test == 'R':
        for vertices, point in vertice_Locations.items():
            if point[0] == coord01L[0] and point[1] == coord01L[1]:
                startpoint = vertices
            if point[0] == coord02L[0] and point[1] == coord02L[2]:
                endpoint = vertices



        reached_paths = least_cost_path(edmonton_Graph, startpoint, endpoint, costObject)
        print('N',len(reached_paths))
        for returns in range(len(reached_paths)):
            returnmsg= input()
            if returnmsg =='A':
                print('W',reached_paths[returns])
        print('E')
