m, s = [int(tmp) for tmp in input().split()]

def find_max(m, s):
    if s == 0:
        if m == 1:
            return 0
        else:
            return -1
    if 9 * m < s:
        return -1
    tmps = s
    out = [0] * m
    ind = 0
    while tmps != 0:
        a = min(tmps, 9)
        out[ind] = a
        tmps -= a
        ind += 1
    return ''.join(str(item) for item in out)

    
def find_min(m, s):
    if s == 0:
        if m == 1:
            return 0
        else:
            return -1
    if 9 * m < s:
        return -1
    if 9 * (m - 1) >= s:
        tmps = s - 1
        out = [1] + [0] * (m - 1)
        ind = m - 1
        while tmps != 0:
            a = min(tmps, 9)
            out[ind] = a
            tmps -= a
            ind -= 1
    else:
        tmps = s
        out = [0] * (m)
        ind = m - 1
        while tmps != 0:
            a = min(tmps, 9)
            out[ind] = a
            tmps -= a
            ind -= 1
        
    return ''.join(str(item) for item in out)

print(find_min(m, s), find_max(m, s))
