n = int(input())
names = []
for cntN in range(n):
    names.append(input().strip())
profits = {name:0 for name in names}
for cntN in range(n):
    a = input().strip()
    am, k = [int(x) for x in input().split()]
    if k == 0:
        continue
    pr = am // k
    profits[a] -= pr * k
    # friends = []
    for cntK in range(k):
        profits[input().strip()] += pr
for name in names:
    print(name, profits[name])
        
