# Uses python3
import sys
import random

def partition3(a, l, r):
    #write your code here
    i = l
    m = l
    n = r
    pivot = a[l]
    while i <= n:
        if a[i] < pivot:
            a[m], a[i] = a[i], a[m]
            m += 1
            i += 1
        elif a[i] > pivot:
            a[i], a[n] = a[n], a[i]
            n -= 1
        else:
            i += 1
            
    return m, n

def randomized_quick_sort_partition3(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    ml, mr = partition3(a, l, r)
    randomized_quick_sort_partition3(a, l, ml - 1);
    randomized_quick_sort_partition3(a, mr + 1, r);

def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j

def randomized_quick_sort_partition2(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m = partition2(a, l, r)
    randomized_quick_sort(a, l, m - 1);
    randomized_quick_sort(a, m + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort_partition3(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
