
# сортировка слиянием
def merge(a, b):
    l1, l2 = len(a), len(b)
    i1, i2, i3 = 0, 0, 0

    c= [0]*(l1 + l2)

    while i1 < l1 and i2 < l2:
        if a[i1] < b[i2]:
            c[i3] = a[i1]
            i3 += 1
            i1 += 1
        else:
            c[i3] = b[i2]
            i3 += 1
            i2 += 1

    while i1 < l1:
        c[i3] = a[i1]
        i3 += 1
        i1 += 1

    while i2 < l2:
        c[i3] = b[i2]
        i3 += 1
        i2 += 1

    return c

def merge_sort(a):
    l = len(a)
    if l <= 1:
        return

    b = list(a[:l//2])
    c = list(a[l//2:])

    merge_sort(b)
    merge_sort(c)

    for i, x in enumerate(merge(b, c)):
        a[i] = x
