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
        current = path[-1]#4
        if current not in visited:
            visited.add(current)
        if len(path) > len(longest_path):
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