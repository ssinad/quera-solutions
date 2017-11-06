n, m = [int(tmp) for tmp in input().split()]
dic = {}
for cnt in range(n):
    k, v = [tmp for tmp in input().split()]
    dic[k] = v
words = input().split()
for word in words:
    if word in dic:
        print(dic[word], end=' kachal! ')
    else:
        print(end='kachal! ')
