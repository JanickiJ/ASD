# Dana jest tablica A liczb wymiernych (wszystkie liczby są różne).
# Proszę podać algorytm, który znajdzie takie dwie liczby A[i] i A[j],
# które po posortowaniu tablicy występują bezpośrednio koło siebie i
# których różnica jest maksymalna.

# bucketsort szukam max diff miedzy min w bucket[i+1]i max bucket[i]

def bucketSort(arr):
    norm = int(max(arr)) + 1
    n = len(arr)
    buckets = [[] for _ in range(norm)]
    max_diff = 0
    result1 = arr[0]
    result1 = arr[1]

    for num in arr:
        norm_num = num / norm
        bucket_idx = int(n * norm_num)
        buckets[bucket_idx].append(num)

    for i in range(0, n):

        while i < n - 1 and not buckets[i]:
            i += 1
        j = i + 1
        while j < n and not buckets[j]:
            j += 1
        if buckets[i] and buckets[j]:
            min_val = min(buckets[j])
            max_val = max(buckets[i])
            if min_val - max_val > max_diff:
                max_diff = min_val - max_val
                result1 = min_val
                result2 = max_val
    return result1, result2


arr = [5.5, 95.3, 8.4, 13.234, 50.01, 90.12, 33.01, 86.31, 82.244, 18.23, 25.15, 75.45, 67.15]
print(bucketSort(arr))
print(sorted(arr))
