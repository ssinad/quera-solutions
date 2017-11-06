from math import floor
def myPow(base, exp):
    return base ** exp
base = float(input())
exp = int(input())
print('{:.3f}'.format( floor( 1000 * myPow(base, exp) ) / 1000))
