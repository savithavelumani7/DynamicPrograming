
def arrays(arr):
    a = arr[0]
    b = arr[0]

    for i in range(1, len(arr)):
        b = max(arr[i], b + arr[i])
        a = max(a, b)
        

    return a

arr=list(map(int,input().split()))
result=arrays(arr)
print(result)
