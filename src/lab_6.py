def minimum_beers(N, B, raw):
    try:
        if not (str(N).isdigit() and str(B).isdigit()):
            raise ValueError("N і B повинні бути цілими додатними числами")

        N, B = int(N), int(B)

        if N <= 0 or B <= 0:
            raise ValueError("Кількість людей і сортів пива повинна бути більшою за 0")

        if len(raw) != N * B:
            raise ValueError(f"Невірна довжина рядка raw")

        if any(c not in 'YN' for c in raw):
            raise ValueError("Рядок raw може містити лише символи Y або N")

    except ValueError as e:
        print(f"Помилка: {e}")
        return None

    likes = [set() for _ in range(B)]

    for i in range(N):
        for j in range(B):
            if raw[i * B + j] == 'Y':
                likes[j].add(i)

    uncovered = set(range(N))
    selected_beers = []

    while uncovered:
        best_beer = -1
        max_covered = 0

        for beer in range(B):
            covered_now = len(likes[beer] & uncovered)
            if covered_now > max_covered:
                max_covered = covered_now
                best_beer = beer

        if best_beer == -1:
            raise ValueError("Не всі п'ють пиво")

        selected_beers.append(best_beer)
        uncovered -= likes[best_beer]

    return len(selected_beers)

if __name__ == '__main__':
    N, B = map(int, input().split())
    raw = input().replace(" ", "")
    print(minimum_beers(N, B, raw))