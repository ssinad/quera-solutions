n = int(input())
for cnt in range(n + 1):
    print(' ' * (n - cnt) + '*' * cnt + '*' + '*' * cnt + ' ' * (n - cnt))
for cnt in range(n - 1, -1, -1):
    print(' ' * (n - cnt) + '*' * cnt + '*' + '*' * cnt + ' ' * (n - cnt))
