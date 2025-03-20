def min_board_size(N, W, H):
    left = max(W, H)
    right = max(W, H) * N

    while left < right:
        mid = (left + right) // 2
        rows = mid // W
        cols = mid // H

        if rows * cols >= N:
            right = mid
        else:
            left = mid + 1

    return left

print(min_board_size(10, 2, 3))  # 9
print(min_board_size(2, 1000000000, 999999999))  # 1999999998
print(min_board_size(4, 1, 1))  # 2
