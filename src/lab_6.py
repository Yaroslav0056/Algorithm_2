from itertools import combinations

def minimum_beers_greedy(N, B, raw):
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

    return selected_beers

def smart_minimum_beers(N, B, raw):
    likes = [set() for _ in range(B)]
    for i in range(N):
        for j in range(B):
            if raw[i * B + j] == 'Y':
                likes[j].add(i)

    greedy_solution = minimum_beers_greedy(N, B, raw)
    best_combo = greedy_solution

    all_valid_beers = [i for i in range(B) if likes[i]]

    for r in range(1, len(greedy_solution)):
        for combo in combinations(all_valid_beers, r):
            covered = set()
            for beer in combo:
                covered |= likes[beer]
            if len(covered) == N:
                return len(combo), list(combo)

    return len(best_combo), best_combo

def main():
    try:
        N_B_input = input("Введіть кількість людей та кількість сортів пива через пробіл: ").split()
        if len(N_B_input) != 2 or not all(i.isdigit() for i in N_B_input):
            raise ValueError("Потрібно ввести два цілих додатних числа через пробіл")
        N, B = map(int, N_B_input)

        raw = input("Введіть переваги: ").replace(" ", "").upper()
        if any(i not in 'YN' for i in raw):
            raise ValueError("Переваги мають містити лише символи Y або N")
        if len(raw) != N * B:
            raise ValueError(f"Невірно введені переваги")

        beer_count, selected_beers = smart_minimum_beers(N, B, raw)
        print(f"Потрібно купити {beer_count} сортів пива")
        print(f"Сорти пива які потрібно купити: {', '.join(map(str, sorted(selected_beers)))}")

    except ValueError as e:
        print(f"Помилка: {e}")

if __name__ == '__main__':
   main()
