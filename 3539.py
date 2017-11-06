def sum_digit(num):
    s = 0
    while num > 0:
        s += num % 10
        num //= 10
    return s
n = int(input())
while not (0 <= n <= 9):
    n = sum_digit(n)
print(n)
