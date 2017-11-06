a = int(input())
arr = []
while a != 0:
    arr.append(a)
    a = int(input())   
for item in arr[::-1]:
        print(item)
