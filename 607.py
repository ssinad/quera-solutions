p, q, r = [int(x) for x in input().split()]
m1 = []
m2 = []
for cnt in range(p):
    m1.append([int(x) for x in input().split()])
for cnt in range(q):
    m2.append([int(x) for x in input().split()])
res = []
for i in range(p):
    row = []
    for j in range(r):
        s = 0
        for k in range(q):
            s += m1[i][k] * m2[k][j]
        print(s, end=' ')
        # row.append(s)
    print()
 #   res.append(row)
#print(res)
            
