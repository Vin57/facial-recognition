from implementation import *

map1 = [[0 for i in range(16)] for j in range(16)]

map1[2][1] = 1
map1[2][3] = 1
map1[2][5] = 1
map1[2][6] = 1
map1[2][8] = 1
map1[2][9] = 1
map1[3][6] = 1
map1[4][3] = 1
map1[5][3] = 1
map1[5][3] = 1
map1[5][6] = 1
map1[5][8] = 1
map1[6][3] = 1
map1[8][3] = 1
map1[8][6] = 1
map1[8][6] = 1
map1[9][8] = 1

example_graph = SimpleGraph()
example_graph.edges = {
    'A': ['B'],
    'B': ['A', 'C', 'G'],
    'C': ['B', 'D'],
    'D': ['E'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['B', 'H'],
    'H': ['I'],
    'I': ['H', 'P'],
    'P': ['I', 'J'],
    'J': ['P']
}


def breadth_first_search(graph: Graph, start: Location):
    # print out what we find
    frontier = Queue()
    frontier.put(start)
    reached: dict[Location, bool] = {}
    reached[start] = True
    
    while not frontier.empty():
        current: Location = frontier.get()
        print("  Visiting %s" % current)
        for next in graph.neighbors(current):
            if next not in reached:
                frontier.put(next)
                reached[next] = True

print('Reachable from A:')
breadth_first_search(example_graph, 'A')
print('Reachable from E:')
breadth_first_search(example_graph, 'E')

def loadmaps(level):
    return breadth_first_search(example_graph)