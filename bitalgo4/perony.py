def size(A):
    return A[0]
def right(i):
    return i*2+1
def left(i):
    return i*2


def heapify(A,i):
    l=left(i)
    r=right(i)
    max=i
    if l<=size(A) and A[l]>A[max]:
        max=l
    if r<=size(A) and A[r]>A[max]:
        max=r
    if max!=i:
        A[i],A[max]=A[max],A[i]
        heapify(A,max)

def build_heap(A):
    for i in range(size(A)//2,0,-1):
        heapify(A,i)

def trains(arr,m):
    heap=[len(arr)-1]
    for i in range(len(arr)):
        heap.append(arr[i][1])
    build_heap(heap)
    i=0
    counter=0
    while i<len(arr):
        if arr[i][0]<heap[1]:
            counter+=1
            i+=1
        elif arr[i][0] == heap[1]:
            heap[1] = heap[heap[0]]
            heap[0] -= 1
            heapify(heap, 1)
            i+=1
        else:
            counter-=1
            heap[1] = heap[heap[0]]
            heap[0]-=1
            heapify(heap,1)
        if counter > m:
            return False
    return True


arr=[(0,10),(1,11),(3,5),(3,6),(8,12),(9,13)]
print(trains(arr,4))
#do poprawy