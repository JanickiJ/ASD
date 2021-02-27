def min_sum(arr):
    arr.sort()
    num1=0
    num2=0
    for i in range(0,len(arr),2):
        num1 = num1 * 10 + arr[i]

    for i in range(1, len(arr), 2):
        num2 = num2 *10 + arr[i]

    return num1+num2

arr=[0,0,0,0,3,2,3,2,1,1]
print(min_sum(arr))
