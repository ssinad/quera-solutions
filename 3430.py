inp = input().strip()
n = len(inp)
print(inp)
for cnt in range(1, n):
    print(inp[cnt] * (cnt + 1) + inp[cnt + 1:])
