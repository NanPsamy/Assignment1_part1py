import server
from graph import Graph

# first load the edmonton graph
edmonton_graph, location = server.load_edmonton_graph("edmonton-roads-2.0.1.txt")

# create the CostDistance instance
cost = server.CostDistance(location)

# now test the distance method from CostDistance
print(cost.distance((1503281720, 29577354)))

# build a test graph
graph = Graph({1,2,3,4,5,6}, [(1,2), (1,3), (1,6), (2,1),
            (2,3), (2,4), (3,1), (3,2), (3,4), (3,6), (4,2), (4,3),
            (4,5), (5,4), (5,6), (6,1), (6,3), (6,5)])

# lengths of the edges described explicitly
weights = {(1,2): 7, (1,3):9, (1,6):14, (2,1):7, (2,3):10,
           (2,4):15, (3,1):9, (3,2):10, (3,4):11, (3,6):2,
           (4,2):15, (4,3):11, (4,5):6, (5,4):6, (5,6):9, (6,1):14,
           (6,3):2, (6,5):9}

# a simple "dummy" class that just uses the weights in the above dictionary
class SimpleDist:
    def distance(self, e): return weights[e]

cost2 = SimpleDist()

# test the least_cost_path function
print(server.least_cost_path(graph, 1, 5, cost2))
