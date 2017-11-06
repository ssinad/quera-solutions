n = int(input())
print('*' * n)
if n > 2:
    for i in range(n - 2):
        print('*' + ' ' * (n - 2) + '*')
if n > 1:
    print('*' * n)
    
