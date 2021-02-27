# w rozwiazaniu będę używał struktury kopca min
def right(i):
    return i * 2 + 1


def left(i):
    return i * 2


def parent(i):
    return i // 2


def size(A):
    return A[0]


def heapify(A, i):
    l = left(i)
    r = right(i)
    min = i
    if l <= size(A) and A[l] < A[min]:
        min = l
    if r <= size(A) and A[r] < A[min]:
        min = r
    if min != i:
        A[i], A[min] = A[min], A[i]
        heapify(A, min)


def build_heap(A):
    B = [0] * (len(A) + 1)
    B[0] = len(A)
    for i in range(len(A)):
        B[i + 1] = A[i]

    for i in range(size(B) // 2, 0, -1):
        heapify(B, i)
    return B


# ilosc potrzebnych bitow bede liczył w taki sposob, że:
# 1. do sumy calkowitej bede dodawał suma1(suma 2 najmniejszych elementow)
# 2. dwa najmniejsze elementy zastąpie elementem o wartosci suma1
# 3. naprawie kopiec
# 4. czynnosc będę powtarzał aż zostanie mi jeden element
# 5. zwróce sume całkowitą

# tworze funkcje która wykona kroki 1,2,3

def sum_2_min(heap):
    size = heap[0]
    if size == 2 or heap[2] <= heap[3]: #wybieram drugi element minimalny lub jesli nie istnieja dwa biore ten który istnieje
        suma1 = heap[1] + heap[2]
        heap[0] -= 1
        heap[1] = suma1
        heap[2] = heap[size]
        heapify(heap, 1)
        heapify(heap, 2)
        return suma1
    else:
        suma1 = heap[1] + heap[3]
        heap[0] -= 1
        heap[1] = suma1
        heap[3] = heap[size]
        heapify(heap, 1)
        heapify(heap, 2)
        return suma1


# tworze funkcje która wykona kroki 4 i 5, z uwzglednieniem przypadkow
# gdzie tablica danych ma długosc 0 lub 1
def huffman_len(A):
    if size(A) == 0:
        return 0
    if size(A) == 1:
        return A[1]
    else:
        heap = build_heap(A)
        print(heap)
        suma_calkowita = 0
        while size(heap) > 1:
            suma1 = sum_2_min(heap)
            suma_calkowita += suma1
        return suma_calkowita


# elementarny test, powinien wypisać 2600
print(huffman_len([16,12,9,45,5,13]))
