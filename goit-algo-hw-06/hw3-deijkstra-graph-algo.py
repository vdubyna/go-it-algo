import networkx as nx
import matplotlib.pyplot as plt

# Створимо граф транспортної мережі між містами України з вагами ребер
G_ukraine_weighted = nx.Graph()

# Додавання вершин (міст)
cities = [
    'Kyiv', 'Lviv', 'Odessa', 'Dnipro', 'Kharkiv',
    'Zaporizhzhia', 'Vinnytsia', 'Chernihiv', 'Ivano-Frankivsk',
    'Uzhhorod', 'Poltava', 'Rivne', 'Kherson', 'Mykolaiv', 'Cherkasy'
]
G_ukraine_weighted.add_nodes_from(cities)

# Додавання ребер з вагами (відстань між містами, умовні дані)
edges_ukraine_weighted = [
    ('Kyiv', 'Lviv', 540), ('Kyiv', 'Vinnytsia', 270), ('Kyiv', 'Chernihiv', 140), ('Kyiv', 'Dnipro', 480),
    ('Lviv', 'Ivano-Frankivsk', 130), ('Lviv', 'Uzhhorod', 260), ('Lviv', 'Rivne', 210),
    ('Odessa', 'Mykolaiv', 130), ('Odessa', 'Kherson', 200), ('Odessa', 'Dnipro', 470),
    ('Dnipro', 'Zaporizhzhia', 85), ('Dnipro', 'Kharkiv', 215), ('Dnipro', 'Poltava', 180),
    ('Vinnytsia', 'Cherkasy', 280), ('Chernihiv', 'Poltava', 310), ('Kharkiv', 'Zaporizhzhia', 260)
]
G_ukraine_weighted.add_weighted_edges_from(edges_ukraine_weighted)

# Візуалізація графа з вагами
def visualize_graph_with_weights(graph, path=None, title="Graph with Weights"):
    plt.figure(figsize=(12, 10))
    pos = nx.spring_layout(graph, seed=42)

    # Візуалізація ребер
    edge_colors = ['red' if (u, v) in path or (v, u) in path else 'gray' for u, v in graph.edges()] if path else 'gray'
    edge_labels = nx.get_edge_attributes(graph, 'weight')

    nx.draw(
        graph, pos, with_labels=True, node_size=800, node_color='lightgreen',
        font_size=16, font_color='black', edge_color=edge_colors, width=2
    )
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_color='blue')
    plt.title(title, fontsize=20)
    plt.show()

# Реалізація алгоритму Дейкстри для пошуку найкоротшого шляху
def dijkstra_shortest_path(graph, start, goal):
    # Використовуємо вбудовану функцію NetworkX для алгоритму Дейкстри
    shortest_path = nx.dijkstra_path(graph, start, goal)
    shortest_path_length = nx.dijkstra_path_length(graph, start, goal)

    # Візуалізація найкоротшого шляху
    visualize_graph_with_weights(graph, list(zip(shortest_path, shortest_path[1:])),
                                 f"Dijkstra Shortest Path from {start} to {goal}")

    return shortest_path, shortest_path_length

# Візуалізація графа з вагами
visualize_graph_with_weights(G_ukraine_weighted, title="Graph with Weights")

# Пошук найкоротшого шляху між двома містами, наприклад, між 'Kyiv' та 'Zaporizhzhia'
start_city = 'Kyiv'
goal_city = 'Zaporizhzhia'

shortest_path, shortest_path_length = dijkstra_shortest_path(G_ukraine_weighted, start_city, goal_city)

print(f"Найкоротший шлях від {start_city} до {goal_city} за алгоритмом Дейкстри: {shortest_path}")
print(f"Довжина найкоротшого шляху: {shortest_path_length} км")