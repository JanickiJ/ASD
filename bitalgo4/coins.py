def coinchange(arr,money):
    counter=0
    i=len(arr)-1
    while money!=0:
        if money < arr[i]:
            i -= 1

        money -= arr[i]
        counter += 1
    return counter

arr=[1,2,5]
print(coinchange(arr,18))