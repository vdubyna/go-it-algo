import networkx as nx
from collections import deque
import matplotlib.pyplot as plt
import time

# Створимо граф транспортної мережі між містами України
G_ukraine = nx.Graph()

# Додавання вершин (міст)
cities = [
    'Kyiv', 'Lviv', 'Odessa', 'Dnipro', 'Kharkiv',
    'Zaporizhzhia', 'Vinnytsia', 'Chernihiv', 'Ivano-Frankivsk',
    'Uzhhorod', 'Poltava', 'Rivne', 'Kherson', 'Mykolaiv', 'Cherkasy'
]
G_ukraine.add_nodes_from(cities)

# Додавання ребер (доріг або маршрутів між містами)
edges_ukraine = [
    ('Kyiv', 'Lviv'), ('Kyiv', 'Vinnytsia'), ('Kyiv', 'Chernihiv'), ('Kyiv', 'Dnipro'),
    ('Lviv', 'Ivano-Frankivsk'), ('Lviv', 'Uzhhorod'), ('Lviv', 'Rivne'),
    ('Odessa', 'Mykolaiv'), ('Odessa', 'Kherson'), ('Odessa', 'Dnipro'),
    ('Dnipro', 'Zaporizhzhia'), ('Dnipro', 'Kharkiv'), ('Dnipro', 'Poltava'),
    ('Vinnytsia', 'Cherkasy'), ('Chernihiv', 'Poltava'), ('Kharkiv', 'Zaporizhzhia')
]
G_ukraine.add_edges_from(edges_ukraine)

# Функція для візуалізації графа з виділенням поточного шляху
def visualize_graph(graph, path, visited, title):
    plt.figure(figsize=(12, 10))
    pos = nx.spring_layout(graph, seed=42)

    # Виділення вершин і ребер
    node_colors = ['lightgreen' if node in visited else 'skyblue' for node in graph.nodes()]
    edge_colors = ['red' if (u, v) in path or (v, u) in path else 'gray' for u, v in graph.edges()]

    nx.draw(
        graph, pos, with_labels=True, node_color=node_colors, node_size=800,
        edge_color=edge_colors, font_size=16, font_color='black'
    )
    plt.title(title, fontsize=20)
    plt.show()
    time.sleep(1)  # Затримка для анімаційного ефекту

# BFS з візуалізацією
def bfs_path(graph, start, goal):
    visited = set()
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        vertex = path[-1]

        if vertex == goal:
            visualize_graph(graph, list(zip(path, path[1:])), visited, f"BFS: шлях до {goal} знайдено")
            return path

        elif vertex not in visited:
            for neighbor in graph[vertex]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

            visited.add(vertex)
            visualize_graph(graph, list(zip(path, path[1:])), visited, f"BFS: обхід вершини {vertex}")

# DFS з візуалізацією
def dfs_path(graph, start, goal, path=None, visited=None):
    if path is None:
        path = [start]
    if visited is None:
        visited = set()
    visited.add(start)

    if start == goal:
        visualize_graph(graph, list(zip(path, path[1:])), visited, f"DFS: шлях до {goal} знайдено")
        return path

    visualize_graph(graph, list(zip(path, path[1:])), visited, f"DFS: обхід вершини {start}")

    for neighbor in graph[start]:
        if neighbor not in visited:
            new_path = dfs_path(graph, neighbor, goal, path + [neighbor], visited)
            if new_path:
                return new_path

# Запуск BFS і DFS з візуалізацією для пошуку шляху між двома містами
start_city = 'Kyiv'
goal_city = 'Zaporizhzhia'

print("Виконується BFS...")
bfs_result = bfs_path(G_ukraine, start_city, goal_city)

print("Виконується DFS...")
dfs_result = dfs_path(G_ukraine, start_city, goal_city)

print(f"BFS шлях від {start_city} до {goal_city}: {bfs_result}")
print(f"DFS шлях від {start_city} до {goal_city}: {dfs_result}")