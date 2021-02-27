def inversion_number(arr):
    mid=len(arr)/2
    sum=0
    for i in range(len(arr)):
        if i<mid and arr[i] == "m" :
            sum+= mid - i
        elif i>mid and arr[i] == "w":
            sum+=i-mid
    return sum

arr=["w","w","w","m","m","m"]
print(inversion_number(arr))