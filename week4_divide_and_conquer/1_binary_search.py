# Uses python3
import sys

def binary_search(a, x):
    # write your code here
    left_point = 0
    right_point = len(a) - 1
    while left_point <= right_point:
        mid_point = (left_point + (right_point - left_point)/2)
        mid_point = int(round(mid_point))
        if x == a[mid_point]:
            return mid_point
        elif x < a[mid_point]:
            right_point = mid_point - 1
        elif x > a[mid_point]:
            left_point = mid_point + 1
    return -1

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')

