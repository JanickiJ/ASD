def suma(arr):
    for i in range(len(arr)):
        for n in range(i, len(arr)):
            if arr[i] + arr[n] == 9:
                return n, i


def twoSum(List, target):
    wynikowa = []
    for i in range(len(List)):
        szukana = target - List[i]
        if szukana in wynikowa:
            x = List.index(szukana)
            return [x, i]
        else:
            wynikowa.append(List[i])


def reverse(x):
    liczba = 0
    mnoznik = 1
    if x < 0:
        mnoznik = -1
        x=x*mnoznik
    while x != 0:
        a = x % 10
        x = x // 10
        liczba = liczba * 10 + a
    return liczba * mnoznik

print(reverse(-123))

