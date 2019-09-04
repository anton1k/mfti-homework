# двоичный поиск
def binary_search(a, x):
    l = 0
    r = len(a)-1

    while l != r:
        m = (l + r)//2
        if x == a[m]:
            return m
        elif x > a[m]:
            l = m + 1
        else:
            r = m - 1

    return l

