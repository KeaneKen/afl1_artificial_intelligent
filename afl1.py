from collections import deque

class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent

class StackFrontier:                    
    def __init__(self):
        self.items = []
    def add(self, node):
        self.items.append(node)
    def contains_state(self, state):
        return any(n.state == state for n in self.items)
    def empty(self):
        return len(self.items) == 0
    def remove(self):
        return self.items.pop()

class QueueFrontier:                      
    def __init__(self):
        self.items = deque()
    def add(self, node):
        self.items.append(node)
    def contains_state(self, state):
        return any(n.state == state for n in self.items)
    def empty(self):
        return len(self.items) == 0
    def remove(self):
        return self.items.popleft()

def graph_search(graph, start, goal, frontier):
    frontier.add(Node(start))
    explored = set()
    order = []              
    while not frontier.empty():
        node = frontier.remove()
        if node.state == goal:
            path = []
            while node:
                path.append(node.state)
                node = node.parent
            return path[::-1], order

        explored.add(node.state)
        order.append(node.state)

        neighbors = sorted(graph[node.state])
        if isinstance(frontier, StackFrontier):
            neighbors.reverse()           # smallest gets popped first

        for n in neighbors:
            if n not in explored and not frontier.contains_state(n):
                frontier.add(Node(n, node))

    return None, order

graph = {
    "Patra Residence":        ["Jembatan Barombong", "Jembatan Kembar Gowa"],
    "Jembatan Barombong":     ["Patra Residence", "Tanjung Bunga"],
    "Jembatan Kembar Gowa":   ["Jalan Sultan Alauddin", "Patra Residence"],
    "Jalan Sultan Alauddin":  ["Jembatan Kembar Gowa", "Tanjung Bunga"],
    "Tanjung Bunga":          ["Jalan Sultan Alauddin", "Jembatan Barombong", "UC Makassar"],
    "UC Makassar":            ["Tanjung Bunga"],
}

print(graph_search(graph, "Patra Residence", "UC Makassar", QueueFrontier()))
print(graph_search(graph, "Patra Residence", "UC Makassar", StackFrontier()))