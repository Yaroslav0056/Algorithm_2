def find_unsorted_subarray(arr):
    if len(arr) <= 1:
        return -1, -1

    left = 0
    while left < len(arr) - 1 and arr[left] <= arr[left + 1]:
        left += 1

    if left == len(arr) - 1:
        return -1, -1

    right = len(arr) - 1
    while right > 0 and arr[right] >= arr[right - 1]:
        right -= 1

    min_value = min(arr[left : right + 1])
    max_value = max(arr[left : right + 1])

    while left > 0 and arr[left - 1] > min_value:
        left -= 1

    while right < len(arr) - 1 and arr[right + 1] < max_value:
        right += 1

    return left, right


if __name__ == "__main__":
    test_arrays = [
        [1, 2, 3, 4, 5],
        [1],
        [5, 4, 3, 2, 1],
        [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19],
        [2, 6, 4, 8, 10, 9, 15],
    ]

    for arr in test_arrays:
        result = find_unsorted_subarray(arr)
        print(f"Масив: {arr}")
        print(f"Індекси невідсортованого підмасиву: {result}\n")
