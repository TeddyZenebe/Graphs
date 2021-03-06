class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)
def earliest_ancestor(ancestors, starting_node):#8
    #test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    plan_to_Visite = Queue()
    plan_to_Visite.enqueue([starting_node])#
    longest_path = []#[8,11]
    visited = set()#{8,11,4}
    while plan_to_Visite.size() > 0:
        path = plan_to_Visite.dequeue()#[8,4]
        print('path', path)
        current = path[-1]#4
        if current not in visited:
            visited.add(current)
        if len(path) > len(longest_path):
            longest_path = path
        elif len(path) == len(longest_path):
            if path[-1] < longest_path[-1]:
                longest_path = path  
        for i in range(len(ancestors)):
            if ancestors[i][1] is current:
                new_path = path.copy()#[8,11]
                new_path.append(ancestors[i][0])
                plan_to_Visite.enqueue(new_path)
        print('longest_path', longest_path)
    earliest = longest_path.pop()#
    if earliest is starting_node:
        earliest = -1
    return earliest

#option 2 using graph
class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")
def earliest_ancestor_Opt2(ancestors, starting_node):
    # Build the graph
    graph = Graph()
    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
        # Build edges in reverse
        graph.add_edge(pair[1], pair[0])
    # Do a BFS (storing the path)
    q = Queue()
    q.enqueue([starting_node])
    max_path_len = 1
    earliest_ancestor = -1
    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]
        # If the path is longer or equal and the value is smaller, or if the path is longer)
        if (len(path) >= max_path_len and v < earliest_ancestor) or (len(path) > max_path_len):
            earliest_ancestor = v
            max_path_len = len(path)
        for neighbor in graph.vertices[v]:
            path_copy = list(path)
            path_copy.append(neighbor)
            q.enqueue(path_copy)
    return earliest_ancestor
