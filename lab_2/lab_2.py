def min_board(N, W, H):
    min_size = max(W, H)
    max_size = max(W, H) * N

    counter = 0
    while min_size < max_size:
        counter += 1
        mid = (min_size + max_size) // 2
        weight = mid // W
        height = mid // H

        if weight * height >= N:
            max_size = mid
        else:
            min_size = mid + 1

    print(f'Розмір сторони квадрату: {min_size}')
    print(f'Кількість ітерацій: {counter}')

min_board(10, 2, 3)
min_board(2_000_000_000, 1000000000, 999999999)
min_board(4, 1, 1)
min_board(15, 1 , 7)
