#Jakub Janicki
# korzystajac z log obliczam x
# robie bucket sort wkładajac do bucketów korzystajac z równomiernego rozłozenia x
# sortuje wewnatrz bucketów insert sortem
# złozonosc czasowa O(n) poniewaz rozłozenie x jest równomierne wiec bucket sort jest linionwy
# poniewaz insert sort jest liniowy dla małych rozmiarów
#pamieciowa złozonosc O(n)

from zad3testy import runtests
import math
    
def fast_sort(tab, a):
    n = len(tab)
    buckets = [[] for _ in range(n + 1)]

    for el in tab:
        x = math.log(el,a)
        bucket_idx = int(x * n)
        buckets[bucket_idx].append(el)
    for bucket in buckets:
        insertionSort(bucket)

    i = 0
    for bucket in buckets:
        for el in bucket:
            tab[i] = el
            i += 1

    return tab

def insertionSort(arr):
    n = len(arr)
    for i in range(n):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1



runtests( fast_sort )
