a = int(input())
b = int(input())


def showFibNth(a, b):
    if  a == 0:
        return
    print(a)
    showFibNth(b - a, a)

showFibNth(a, b)
