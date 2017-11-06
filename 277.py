n = input()
l = len(n)
a = ['1'] * l
for cnt in range(l):
    if int(n[cnt]) > int(a[cnt]):
        break
    elif int(n[cnt]) < int(a[cnt]):
        a[cnt] = '0'
out = int(''.join(a), 2)
print(out)
