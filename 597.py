# 1, 2, 3, 4, 5, 6, 7, 8, 9
# 0, 1, 1, -1, -1, 2, 2, -2, -2
# 0, 0, 1, 1, -1, -1, 2, 2, -2, -2
def seq(n):
    a = (n - 1) // 2
    b = (n + 1) // 4
    if a % 2 == 0:
        return -b
    else:
        return b
n = int(input())
x = seq(n + 1)
y = seq(n)
print(x, y)
