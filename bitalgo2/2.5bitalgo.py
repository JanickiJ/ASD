#Zaimplementuj funkcję average_score(arr, n, lowest, highest). Fu
#nkcja ta przyjmuje na wejściu tablicę n liczb rzeczywistych (ich rozkład nie jest znany,
#ale wszystkie są parami różne) i zwraca średnią wartość podanych liczb po odrzuceniu lowest najmniejszych oraz highest największych.
#Zaimplementowana funkcja powinna być możliwie jak najszybsza. Oszacuj jej złożoność czasową (oraz bardzo krótko uzasadnić to oszacowanie).

def parent(i):
    return i // 2


def left_son(i):
    return i * 2


def right_son(i):
    return i * 2 + 1


def size(k):
    return k[0]


def heapify_max(k, i):
    l = left_son(i)
    r = right_son(i)
    maks = i
    if l <= size(k) and k[maks] < k[l]:
        maks = l
    if r <= size(k) and k[maks] < k[r]:
        maks = r
    if maks != i:
        k[i], k[maks] = k[maks], k[i]
        heapify_max(k, maks)

def heapify_min(k, i):
    l = left_son(i)
    r = right_son(i)
    min = i
    if l <= size(k) and k[min] > k[l]:
        min = l
    if r <= size(k) and k[min] > k[r]:
        min = r
    if min != i:
        k[i], k[min] = k[min], k[i]
        heapify_min(k, min)

def averange_score(arr, lowest, highest):
    heap_min = [highest]
    heap_max = [lowest]
    for i in range(1, lowest+1):
        heap_max.append(10000)
    for i in range(1, highest+1):
        heap_min.append(0)
    sum=0
    for i in range(len(arr)):
        sum+=arr[i]
        if arr[i] < heap_max[1]:
            heap_max[1] = arr[i]
            heapify_max(heap_max, 1)
        if arr[i] > heap_min[1]:
            heap_min[1] = arr[i]
            heapify_min(heap_min, 1)
    sum1=0
    sum2=0
    for i in range(1,len(heap_max)):
        sum1+=heap_max[i]
    for i in range(1,len(heap_min)):
        sum2+=heap_min[i]
    result_sum=sum-sum1-sum2
    return result_sum


arr=[14,10,3,2,5,4,6,1,7,8,9,11,13,15,16,12]
print(averange_score(arr, 5 , 5))
