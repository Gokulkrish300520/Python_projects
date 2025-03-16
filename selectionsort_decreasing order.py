arr = list(map(int, input().split()))
for i in range(len(arr)-1):
    maximum = i
    for j in range(i+1, len(arr)):
        if arr[maximum] < arr[j]:
            maximum = j
    temp = arr[maximum]
    arr[maximum] = arr[i]
    arr[i] = temp

print(arr)