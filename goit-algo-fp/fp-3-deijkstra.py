import heapq
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}

    def add_node(self, value):
        self.nodes.add(value)
        self.edges[value] = {}

    def add_edge(self, from_node, to_node, weight):
        if from_node in self.edges and to_node in self.edges:
            self.edges[from_node][to_node] = weight

def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph.nodes}
    distances[start] = 0
    predecessors = {node: None for node in graph.nodes}
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph.edges[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, predecessors

def shortest_path(predecessors, start, goal):
    path = []
    step = goal
    while step:
        path.append(step)
        step = predecessors[step]
    return path[::-1]

def visualize_graph(graph, shortest_path=None):
    G = nx.DiGraph()

    # Додаємо вузли і ребра у граф з вагами
    for node, neighbors in graph.edges.items():
        for neighbor, weight in neighbors.items():
            G.add_edge(node, neighbor, weight=weight)

    # Позиції вузлів визначаємо після створення графа
    pos = nx.spring_layout(G)

    # Відображаємо граф
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Виділяємо найкоротший шлях
    if shortest_path:
        path_edges = list(zip(shortest_path, shortest_path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)

    plt.show()

# Приклад використання
graph = Graph()
for node in ['A', 'B', 'C', 'D', 'E']:
    graph.add_node(node)

graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 4)
graph.add_edge('B', 'C', 2)
graph.add_edge('B', 'D', 5)
graph.add_edge('C', 'D', 1)
graph.add_edge('D', 'E', 3)

# Знаходимо найкоротші шляхи від 'A'
start_node = 'A'
distances, predecessors = dijkstra(graph, start_node)

# Приклад пошуку шляху до конкретної вершини
goal_node = 'E'
path = shortest_path(predecessors, start_node, goal_node)

# Візуалізація графа з виділенням найкоротшого шляху
visualize_graph(graph, shortest_path=path)

print("Відстані від вершини", start_node)
for node, distance in distances.items():
    print(f"Від {start_node} до {node}: {distance}")
print(f"Найкоротший шлях від {start_node} до {goal_node}: {' -> '.join(path)}")