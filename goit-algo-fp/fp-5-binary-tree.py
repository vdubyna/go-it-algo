import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def build_binary_tree():
    """Побудова простого бінарного дерева для демонстрації обходу."""
    root = Node(0)
    root.left = Node(1)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    return root

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    """Додає вузли та ребра до графа."""
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    """Малює дерево з кольорами вузлів, що представляють порядок обходу."""
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    node_colors = [tree.nodes[node]["color"] for node in tree.nodes()]
    labels = {node: tree.nodes[node]["label"] for node in tree.nodes()}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos, labels=labels, arrows=False, node_size=2500, node_color=node_colors)
    plt.show()

def count_nodes(node):
    """Підраховує кількість вузлів у дереві."""
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

def generate_colors(n):
    """Генерує градієнт кольорів від темного до світлого."""
    colors = []
    for i in range(n):
        intensity = int(255 * (i / n))  # Від темного до світлого
        color = f'#{intensity:02x}{intensity:02x}{255:02x}'  # Відтінок синього
        colors.append(color)
    return colors

def bfs_traversal(tree_root):
    """Обхід в ширину (BFS) з візуалізацією кожного кроку."""
    queue = deque([tree_root])
    num_nodes = count_nodes(tree_root)
    colors = generate_colors(num_nodes)  # Генерація кольорів для всіх вузлів

    index = 0
    while queue:
        node = queue.popleft()
        node.color = colors[index]
        index += 1

        # Візуалізація на кожному кроці
        draw_tree(tree_root)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

def dfs_traversal(tree_root):
    """Обхід в глибину (DFS) з візуалізацією кожного кроку."""
    stack = [tree_root]
    num_nodes = count_nodes(tree_root)
    colors = generate_colors(num_nodes)  # Генерація кольорів для всіх вузлів

    index = 0
    while stack:
        node = stack.pop()
        node.color = colors[index]
        index += 1

        # Візуалізація на кожному кроці
        draw_tree(tree_root)

        if node.right:  # Спочатку додаємо правий, щоб лівий був зверху в стеку
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

# Побудова дерева
tree_root = build_binary_tree()

# Обхід в ширину (BFS)
print("Обхід в ширину (BFS):")
bfs_traversal(tree_root)

# Відновлення кольору для вузлів перед обходом в глибину
tree_root = build_binary_tree()

# Обхід в глибину (DFS)
print("Обхід в глибину (DFS):")
dfs_traversal(tree_root)