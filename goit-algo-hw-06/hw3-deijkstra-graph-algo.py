import networkx as nx
import heapq

# Create a weighted graph for the transportation network between cities in Ukraine
G_ukraine_weighted = nx.Graph()

# Add nodes (cities)
cities = [
    'Kyiv', 'Lviv', 'Odessa', 'Dnipro', 'Kharkiv',
    'Zaporizhzhia', 'Vinnytsia', 'Chernihiv', 'Ivano-Frankivsk',
    'Uzhhorod', 'Poltava', 'Rivne', 'Kherson', 'Mykolaiv', 'Cherkasy'
]
G_ukraine_weighted.add_nodes_from(cities)

# Add edges with weights (distance between cities, assumed data)
edges_ukraine_weighted = [
    ('Kyiv', 'Lviv', 540), ('Kyiv', 'Vinnytsia', 270), ('Kyiv', 'Chernihiv', 140), ('Kyiv', 'Dnipro', 480),
    ('Lviv', 'Ivano-Frankivsk', 130), ('Lviv', 'Uzhhorod', 260), ('Lviv', 'Rivne', 210),
    ('Odessa', 'Mykolaiv', 130), ('Odessa', 'Kherson', 200), ('Odessa', 'Dnipro', 470),
    ('Dnipro', 'Zaporizhzhia', 85), ('Dnipro', 'Kharkiv', 215), ('Dnipro', 'Poltava', 180),
    ('Vinnytsia', 'Cherkasy', 280), ('Chernihiv', 'Poltava', 310), ('Kharkiv', 'Zaporizhzhia', 260)
]
G_ukraine_weighted.add_weighted_edges_from(edges_ukraine_weighted)

def dijkstra_shortest_path(graph, start, goal):
    # Extract edges formatted as (u, v, w)
    edges = [(u, v, d['weight']) for u, v, d in graph.edges(data=True)]

    # Build the graph dictionary from edges
    graph_dict = {}
    for u, v, w in edges:
        if u not in graph_dict:
            graph_dict[u] = {}
        if v not in graph_dict:
            graph_dict[v] = {}
        graph_dict[u][v] = w
        graph_dict[v][u] = w  # Assuming the graph is undirected

    # Initialize distances and predecessors
    distances = {node: float('infinity') for node in graph_dict}
    distances[start] = 0
    predecessors = {node: None for node in graph_dict}
    priority_queue = [(0, start)]

    # Implementing the priority queue
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node == goal:
            path = []
            step = goal
            while step:
                path.append(step)
                step = predecessors[step]
            return path[::-1], distances[goal]

        for neighbor, weight in graph_dict[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return [], float('infinity')  # if the goal is not reachable

# Usage
start_city = 'Kyiv'
goal_city = 'Zaporizhzhia'
shortest_path, shortest_path_length = dijkstra_shortest_path(G_ukraine_weighted, start_city, goal_city)
print(f"Shortest path from {start_city} to {goal_city}: {shortest_path}")
print(f"Path length: {shortest_path_length} km")