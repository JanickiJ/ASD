
def missing_element(arr):
    diff=arr[0]
    p=0
    q=len(arr)
    while p<q:
        mid=(p+q)//2
        if arr[mid] - mid == diff and mid+1<len(arr) and arr[mid+1]-(mid+1) != diff:
            return arr[mid]+1
        elif arr[mid] - mid == diff:
            p=mid+1
        elif arr[mid] - mid != diff:
            q=mid-1

    return False

arr=[1,2,3,4,5,7,8,9]
print(missing_element(arr))