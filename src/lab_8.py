import matplotlib.pyplot as plt
import networkx as nx


def read_input(file_name):
    input_info = []
    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            values = line.strip().split(",")
            if len(values) == 3:
                input_info.append(values)
    return input_info


def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]


def union(x, y, parent, rank):
    root_x = find(x, parent)
    root_y = find(y, parent)
    if root_x == root_y:
        return False
    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    else:
        parent[root_y] = root_x
        if rank[root_x] == rank[root_y]:
            rank[root_x] += 1
    return True


def draw_graph(edges, highlight_edges=None):
    G = nx.Graph()
    for u, v, w in edges:
        G.add_edge(u, v, weight=int(w))

    pos = nx.spring_layout(G, seed=40)

    weights = nx.get_edge_attributes(G, "weight")
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color="blue",
        edge_color="gray",
        node_size=700,
    )
    nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)

    if highlight_edges:
        nx.draw_networkx_edges(
            G, pos, edgelist=highlight_edges, edge_color="red", width=2
        )

    plt.show()


def min_length_connection(connections):
    sorted_connections = sorted(connections, key=lambda x: int(x[2]))

    parent = {}
    rank = {}
    total_length = 0
    all_nodes = set()
    used_edges = []

    for u, v, _ in sorted_connections:
        all_nodes.add(u)
        all_nodes.add(v)
        if u not in parent:
            parent[u] = u
            rank[u] = 0
        if v not in parent:
            parent[v] = v
            rank[v] = 0

    for u, v, dist in sorted_connections:
        if union(u, v, parent, rank):
            total_length += int(dist)
            used_edges.append((u, v, dist))

    roots = set(find(node, parent) for node in all_nodes)
    if len(roots) != 1:
        return -1, used_edges

    return total_length, used_edges


def calculate_minimal_length(file_name):
    connections = read_input(file_name)

    draw_graph(connections)

    total_length, used_edges = min_length_connection(connections)

    draw_graph(connections, highlight_edges=used_edges)

    print("Використані з'єднання:")
    for u, v, dist in used_edges:
        print(f"{u} - {v} (довжина: {dist})")
    print(f"Сумарна довжина: {total_length}")
    return total_length


if __name__ == "__main__":
    calculate_minimal_length("../data_test/communication_wells.csv")
