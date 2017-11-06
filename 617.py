n = input()
a = int(n)
'''
rev = 0
for chra in n[::-1]:
    rev *= 10
    rev += int(chra)
if a == rev:
    print('YES')
else:
    print('NO')
'''
digits = []
while a > 0:
    digits.append(a % 10)
    a /= 10
l = len(digits)
for cnt in range(l):
    if digits[cnt] != digits[l - cnt - 1] :
        break
else:
    print('NO')
print('YES')
