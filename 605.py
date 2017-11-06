a = 1
b = 2
n = int(input())
if n == 1:
    print(a)
elif n == 2:
    print(b)
else:
    for cnt in range(n - 2):
        c = a + b
        a = b
        b = c
    print(c)
    
