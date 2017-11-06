n = int(input())
m = int(input())
print(sum
      ( (i + j) ** 3 / j ** 2 for i in range(-10, m + 1) for j in range(1, n + 1)
         ))
