def minimum_beers(N, B, raw):
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

def main():
    try:
        N_B_input = input("Введіть кількість людей та кількість сортів пива через пробіл: ").split()
        if len(N_B_input) != 2 or not all(s.isdigit() for s in N_B_input):
            raise ValueError("Потрібно ввести два цілих додатних числа через пробіл")
        N, B = map(int, N_B_input)

        raw = input("Введіть переваги: ").replace(" ", "").upper()
        if any(c not in 'YN' for c in raw):
            raise ValueError("Переваги мають містити лише символи Y або N")
        if len(raw) != N * B:
            raise ValueError(f"Невірно введені переваги")

        result = minimum_beers(N, B, raw)
        if result is not None:
            print(result)

    except ValueError as e:
        print(f"Помилка: {e}")

if __name__ == '__main__':
   main()
