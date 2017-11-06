def palindrome(n):
    return int(str(n)[::-1])

def compare2(x, y):
    a, b = palindrome(x), palindrome(y)
    if a < b:
        return '<'
    elif a == b:
        return '='
    else:
        return '>'

def compare(x, y):
    equal = True
    greater = True
    tx = x
    ty = y 
    for cnt in range(3):
        a = tx % 10
        b = ty % 10
        # print(a, b)
        if not a == b:
            equal = False
            if a < b:
                greater = False
            break
        tx //= 10
        ty //= 10
    if equal or greater:
        maxi = x
        mini = y
    else:
        maxi = y
        mini = x
    if equal:
        return '{} = {}'.format(mini, maxi)
    else:
        return '{} < {}'.format(mini, maxi)
    
        
a = int(input())
b = int(input())
print(compare(b, a))

