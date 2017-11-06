a = input()
b = int(input())
c = int(input())
result = 0
for ch in a:
    result *= b
    result += int(ch)
x = []
while result > 0:
    x.append(result % c)
    result //= c
if x[:] == x[::-1]:
    print('YES')
else:
    print('NO')
