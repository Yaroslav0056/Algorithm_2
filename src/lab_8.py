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


def min_length_connection(connections):
    connections.sort(key=lambda x: int(x[2]))

    parent = {}
    rank = {}
    total_length = 0
    all_nodes = set()
    used_edges = []

    for u, v, _ in connections:
        all_nodes.add(u)
        all_nodes.add(v)
        if u not in parent:
            parent[u] = u
            rank[u] = 0
        if v not in parent:
            parent[v] = v
            rank[v] = 0

    for u, v, dist in connections:
        if union(u, v, parent, rank):
            total_length += int(dist)
            used_edges.append((u, v, dist))

    roots = set(find(node, parent) for node in all_nodes)

    if len(roots) != 1:
        return -1

    if __name__ == "__main__":
        print("Використані з'єднання:")
        for u, v, dist in used_edges:
            print(f"{u} - {v} (довжина: {dist})")
        print("Сумарна довжина:")

    return total_length


def calculate_minimal_length(file_name):
    connections = read_input(file_name)
    return min_length_connection(connections)


if __name__ == "__main__":
    print(calculate_minimal_length("../test/communication_wells.csv"))
