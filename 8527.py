n = int(input())
arr = [int(x) for x in input().split()]
ind = [arr[0] > arr[1]]
for cnt in range(1, n - 1): 
    ind.append(arr[cnt-1] < arr[cnt] > arr[cnt + 1])
ind.append(arr[-2] < arr[-1])
print(ind)
