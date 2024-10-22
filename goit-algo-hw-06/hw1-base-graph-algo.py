import networkx as nx
import matplotlib.pyplot as plt

# Створимо граф, що моделює транспортну мережу між містами України
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

# Візуалізація графа
plt.figure(figsize=(12, 10))
pos = nx.spring_layout(G_ukraine, seed=42)
nx.draw(
    G_ukraine, pos, with_labels=True, node_size=800, node_color='lightgreen',
    font_size=16, font_color='black', edge_color='gray'
)
plt.title("Транспортна мережа міст України", fontsize=20)
plt.show()

# Аналіз основних характеристик графа
num_nodes_ukraine = G_ukraine.number_of_nodes()
num_edges_ukraine = G_ukraine.number_of_edges()
degree_info_ukraine = dict(G_ukraine.degree())
degree_centrality_ukraine = nx.degree_centrality(G_ukraine)

print(f"Кількість вершин: {num_nodes_ukraine}")
print(f"Кількість ребер: {num_edges_ukraine}")
print(f"Вага кожної вершини: {degree_info_ukraine}")
print(f"Центральність за ступенем кожної вершини: {degree_centrality_ukraine}")