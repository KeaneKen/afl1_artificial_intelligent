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
            neighbors.reverse()          

        for n in neighbors:
            if n not in explored and not frontier.contains_state(n):
                frontier.add(Node(n, node))

    return None, order

graph = {
    "Patra Residence":        ["Jalan Andi Mappainga", "Jalan Permandian Alam"],
    "Jalan Andi Mappainga":   ["Patra Residence", "Taman Panciro Indah"],
    "Taman Panciro Indah":    ["Jalan Andi Mappainga", "Jembatan Kembar Gowa"],
    "Jembatan Kembar Gowa":   ["Jalan Sultan Alauddin", "Taman Panciro Indah"],
    "Jalan Sultan Alauddin":  ["Jembatan Kembar Gowa", "Tanjung Bunga"],
    "Jalan Permandian Alam":   ["Patra Residence", "Jembatan Barombong"],
    "Jembatan Barombong":     ["Patra Residence", "Tanjung Bunga"],
    "Tanjung Bunga":          ["Jalan Sultan Alauddin", "Jembatan Barombong", "UC Makassar"],
    "UC Makassar":            ["Tanjung Bunga"],
}

print("BFS:", graph_search(graph, "Patra Residence", "UC Makassar", QueueFrontier()))
print("DFS:", graph_search(graph, "Patra Residence", "UC Makassar", StackFrontier()))