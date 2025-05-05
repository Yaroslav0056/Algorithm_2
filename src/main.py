from big_data import minimum_beers, tqdm, bitarray, randint, random, perf_counter

def generate_preferences(N, B, like_percent, filename, log):
    prob = like_percent / 100
    with open(filename, 'w') as file:
        for _ in tqdm(range(N), desc=f"Генерація {log} матриці"):
            row = bitarray(B)
            for i in range(B):
                row[i] = 1 if random() < prob else 0
            if not row.any():
                row[randint(0, B - 1)] = 1
            file.write(' '.join(str(int(b)) for b in row) + '\n')

def read_preferences(filename, N, B):
    preferences = []
    with open(filename, 'r') as file:
        for line in tqdm(file, total=N, desc="Зчитування матриці", unit="рядок"):
            row = bitarray(B)
            values = list(map(int, line.split()))
            row.setall(False)
            for i, value in enumerate(values):
                row[i] = value
            preferences.append(row)
    return preferences

def main():
    print("Оберіть тип матриці:")
    print("1 - Розріджена")
    print("2 - Щільна")
    print("3 - Випадкова")
    print("4 - Працювати з матрицею та що у файлі")
    choice = input("Ваш вибір: ").strip()

    if choice != '4':
        try:
            N = int(input("Кількість працівників (N): "))
            B = int(input("Кількість сортів пива (B): "))
            assert 0 < N <= 10 ** 6
            assert 0 < B <= 10 ** 5
        except AssertionError:
            print("Некоректні вхідні дані. N ≤ 10^6, B ≤ 10^5")
            exit()

    filename = "matrix.txt"

    if choice == '1':
        generate_preferences(N, B, like_percent=1, filename=filename, log = 'розрідженої')
        preferences = read_preferences(filename, N, B)
    elif choice == '2':
        generate_preferences(N, B, like_percent=15, filename=filename, log = 'щільної')
        preferences = read_preferences(filename, N, B)
    elif choice == '3':
        generate_preferences(N, B, like_percent=50, filename=filename, log = 'випадкової')
        preferences = read_preferences(filename, N, B)
    elif choice == '4':
        with open(filename, 'r') as file:
            first_line = file.readline()
            B = len(first_line.split())
            file.seek(0)
            N = sum(1 for _ in file)

        preferences = read_preferences(filename, N, B)

    else:
        print("Невірний вибір. Введіть 1, 2, 3 або 4")
        exit()

    start = perf_counter()
    result = minimum_beers(N, B, preferences)
    duration = perf_counter() - start

    print(f"\nМінімальна кількість пива: {result}")
    print(f"Час виконання: {duration:.2f} с")

if __name__ == "__main__":
    main()