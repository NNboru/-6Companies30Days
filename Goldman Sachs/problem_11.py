def findTwoElement(arr, n): 
    arr.sort()
    a,b=-1,-1
    for i in range(n-1):
        if arr[i]==arr[i+1]:
            a=arr[i]
        if arr[i+1]-arr[i]==2:
            b=arr[i]+1
    if b==-1:
        if arr[0]==1:
            b=n
        else:
            b=1
    return (a,b)


if __name__=='__main__':
    print(*findTwoElement([1, 3, 3],3))
