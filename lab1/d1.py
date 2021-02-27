# Implementacja jednoczesnego obliczania minimum i maksimum
# w tablicy n eleentowej przy pomocy 3/2 n porównan elementów

def compare3(arr):
    arr_min = []
    arr_max = []

    for i in range(1, len(arr), 2):
        if arr[i] < arr[i - 1]:
            arr_min.append(arr[i])
            arr_max.append(arr[i - 1])
        else:
            arr_min.append(arr[i - 1])
            arr_max.append(arr[i])

    if i == len(arr) - 2:
        odd_element = True

    min_val = arr_min[0]
    max_val = arr_max[0]

    for i in range(len(arr) // 2):
        if arr_max[i] > max_val:
            max_val = arr_max[i]

    for i in range(len(arr) // 2):
        if arr_min[i] < min_val:
            min_val = arr_min[i]

    if odd_element:
        if min_val > arr[len(arr) - 1]:
            min_val = arr[len(arr) - 1]
        elif max_val < arr[len(arr) - 1]:
            max_val = arr[len(arr) - 1]

    return min_val, max_val


arr = [2345, 40, 45, 12, 333, 4566, 2]
print(compare3(arr))
