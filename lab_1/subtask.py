def find_unsorted_subarrays(arr):
    if len(arr) <= 1:
        return -1, -1

    subarrays = []
    i = 0

    while i < len(arr) - 1:
        # Знаходимо початок невідсортованого підмасиву
        while i < len(arr) - 1 and arr[i] <= arr[i + 1]:
            i += 1

        if i == len(arr) - 1:
            break  # Якщо дійшли до кінця, то масив відсортований

        start = i

        # Знаходимо кінець невідсортованого підмасиву
        while i < len(arr) - 1 and arr[i] >= arr[i + 1]:
            i += 1

        end = i
        subarrays.append((start, end))

    return subarrays if subarrays else (-1, -1)


if __name__ == '__main__':
    test_arrays = [
        [1, 2, 3, 6, 5, 4, 7, 8, 9, 12, 11, 10, 13],  # Очікуваний результат: [(3, 5), (9, 11)]
        [1, 2, 3, 4, 5],  # Очікуваний результат: (-1, -1)
        [1],  # Очікуваний результат: (-1, -1)
        [5, 4, 3, 2, 1],  # Очікуваний результат: [(0, 4)]
        [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19],  # Очікуваний результат: [(5, 9)]
        [2, 6, 4, 8, 10, 9, 15],  # Очікуваний результат: [(1, 5)]
    ]

    for arr in test_arrays:
        result = find_unsorted_subarrays(arr)
        print(f"Масив: {arr}")
        print(f"Індекси невідсортованих підмасивів: {result}\n")
