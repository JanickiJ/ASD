def subset(arr1, arr2):
    arr1.sort()
    arr2.sort()

    counter=0
    for i in range(len(arr1)):
        if arr1[i] == arr2[counter]:
            counter+=1
            if counter == len(arr2)-1:
                return True
    return False

arr1=[0,9,8,7,6,5,4,3,2,1,11,12,90,78]
arr2=[12,9,78,23]
arr1.sort()
arr2.sort()
print(subset(arr1,arr2))
