# интерполяционный поиск
import math

def interpolation_search(a, x):
    l = 0
    r = len(a)-1
    
    while l != r:
        m = math.ceil(l + (x - a[l]) / (a[r]-a[l]) * (r - l))
        if x == a[m]:
            return m
        elif x > a[m]:
            l = m + 1
        else:
            r = m-1
            
    return l
