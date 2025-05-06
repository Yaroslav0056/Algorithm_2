from random import random, randint
from bitarray import bitarray
from time import perf_counter
from tqdm import tqdm


def generate_dense_preferences(N, B, like_percent):
    prob = like_percent / 100
    preferences = []
    for _ in tqdm(range(N), desc="Генерація матриці вподобань"):
        row = bitarray(B)
        for i in range(B):
            row[i] = 1 if random() < prob else 0
        if not row.any():
            row[randint(0, B - 1)] = 1
        preferences.append(row)
    return preferences


def liked_by_beer(n, b, prefs):
    liked = [bitarray(n) for _ in range(b)]
    for arr in liked:
        arr.setall(False)
    for i, row in enumerate(prefs):
        for j, val in enumerate(row):
            if val:
                liked[j][i] = 1
    return liked


def greedy(N, B, liked_by):
    uncovered = bitarray(N)
    uncovered.setall(True)
    selected = set()

    while uncovered.any():
        best_beer = -1
        best_coverage = -1

        for b in range(B):
            if b in selected:
                continue
            new_coverage = (liked_by[b] & uncovered).count()
            if new_coverage > best_coverage:
                best_coverage = new_coverage
                best_beer = b

        if best_beer == -1:
            break

        selected.add(best_beer)
        uncovered &= ~liked_by[best_beer]

    return selected


def optimization(n, liked, selected):
    selected = set(selected)
    changed = True

    while changed:
        changed = False
        for beer in list(selected):
            test = selected - {beer}
            cover = bitarray(n)
            cover.setall(False)
            for bb in test:
                cover |= liked[bb]
            if cover.all():
                selected = test
                changed = True
                break
    return selected


def minimum_beers(N, B, preferences):
    liked = liked_by_beer(N, B, preferences)
    greedy_set = greedy(N, B, liked)
    result = optimization(N, liked, greedy_set)
    return len(result)


def main():
    print("Оберіть тип матриці:")
    print("1 - Розріджена")
    print("2 - Щільна")
    print("3 - Випадкова")
    choice = input("Ваш вибір: ").strip()

    try:
        N = int(input("Кількість працівників (N): "))
        B = int(input("Кількість сортів пива (B): "))
        assert 0 < N <= 10**6
        assert 0 < B <= 10**5
    except AssertionError:
        print("Некоректні вхідні дані. N ≤ 10^6, B ≤ 10^5")
        exit()

    if choice == "1":
        preferences = generate_dense_preferences(N, B, like_percent=1)
    elif choice == "2":
        preferences = generate_dense_preferences(N, B, like_percent=15)
    elif choice == "3":
        preferences = generate_dense_preferences(N, B, like_percent=50)
    else:
        print("Невірний вибір. Введіть 1, 2 або 3")
        exit()

    start = perf_counter()
    result = minimum_beers(N, B, preferences)
    duration = perf_counter() - start

    print(f"\nМінімальна кількість пива: {result}")
    print(f"Час виконання: {duration:.2f} с")


if __name__ == "__main__":
    main()
