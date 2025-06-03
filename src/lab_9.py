from math import sqrt


def max_dp(w, lst):

    n = len(lst)

    dp = [[0.0] * (lst[i] + 1) for i in range(n)]

    for i in range(1, n):
        for h in range(1, lst[i] + 1):
            max_val = 0.0
            for h_prev in range(1, lst[i - 1] + 1):
                hypo = sqrt((h - h_prev) ** 2 + w**2)
                max_val = max(max_val, dp[i - 1][h_prev] + hypo)
            dp[i][h] = max_val

    result = max(dp[n - 1][h] for h in range(1, lst[n - 1] + 1))
    return round(result, 2), dp


def write(file_name, dp):

    with open(file_name, "w", encoding="UTF-8") as f:
        f.write("Таблиця динамічного програмування:\n")
        for row in dp:
            f.write(str(row) + "\n")


def main():
    while True:
        print("Виберіть варіант вводу:")
        print("1 - Тестові дані")
        print("2 - Дані з клавіатури")
        print("3 - Вийти з програми")
        inp = input()
        if inp == "1":
            versions = [
                [2, [3, 3, 3]],
                [100, [1, 1, 1, 1]],
                [44, [4, 55, 4, 22, 45]],
            ]
            for idx, version in enumerate(versions, start=1):
                print(f"Варіант {idx}")
                print(
                    f"Відстань між стовпами - {version[0]}, "
                    f"максимальна висота стовпів - {version[1]}"
                )
                result, dp = max_dp(*version)
                print("Максимальна довжина за вашими даними:")
                print(f"\033[92m{result}\033[0m", "\n")
                file_name = f"results/version_{idx}.txt"
                write(file_name, dp)
        elif inp == "2":
            w = int(input())
            lst = list(map(int, input().split()))
            result, dp = max_dp(w, lst)
            print("Максимальна довжина за вашими даними:")
            print(f"\033[92m{result}\033[0m", "\n")
            write("results/your_file.txt", dp)
        elif inp == "3":
            print("До побачення")
            break
        else:
            print("Не має такого!\n")


if __name__ == "__main__":
    main()
