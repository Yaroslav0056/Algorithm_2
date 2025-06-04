from collections import deque

row_moves = [2, 2, -2, -2, 1, 1, -1, -1]
col_moves = [-1, 1, 1, -1, 2, -2, 2, -2]


def is_in(x, y, N, visited):
    return 0 <= x < N and 0 <= y < N and not visited[x][y]


def bfs(N, start, end):
    visited = [[False] * N for _ in range(N)]
    parent = [[None] * N for _ in range(N)]

    q = deque()
    start_x, start_y = start
    end_x, end_y = end
    q.append((start_x, start_y, 0))
    visited[start_x][start_y] = True

    while q:
        x, y, dist = q.popleft()

        if (x, y) == (end_x, end_y):
            return dist, parent

        for move_x, move_y in zip(row_moves, col_moves):
            new_x = x + move_x
            new_y = y + move_y

            if is_in(new_x, new_y, N, visited):
                visited[new_x][new_y] = True
                parent[new_x][new_y] = (x, y)
                q.append((new_x, new_y, dist + 1))

    return -1, parent


def reconstruct_path(parent, start, end):
    path = []
    current = end
    while current != start:
        path.append(current)
        current = parent[current[0]][current[1]]
    path.append(start)
    path.reverse()
    return path


def main():
    with open("../data/input.txt", "r") as f:
        N = int(f.readline())
        start_x, start_y = map(int, f.readline().strip().split(","))
        end_x, end_y = map(int, f.readline().strip().split(","))

    min_steps, parent = bfs(N, (start_x, start_y), (end_x, end_y))

    with open("../data/output.txt", "w", encoding="UTF-8") as f:
        f.write(f"Мінімальна кількість кроків: {min_steps}\n")

    if min_steps != -1:
        path = reconstruct_path(parent, (start_x, start_y), (end_x, end_y))
        with open("../data/output.txt", "a", encoding="UTF-8") as f:
            f.write("Шлях: \n")
            for step in path:
                f.write(f"({step[0]}, {step[1]})\n")
    else:
        print("Шлях не знайдено")
        with open("../data/output.txt", "a", encoding="UTF-8") as f:
            f.write("Шлях не знайдено\n")


if __name__ == "__main__":
    main()
