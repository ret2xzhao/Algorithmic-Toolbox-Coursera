# Uses python3
import sys

def get_change(m):
    #write your code here
    num_10 = m // 10
    num_5 = (m % 10) // 5
    num_1 = ((m % 10) % 5) // 1
    m = num_10 + num_5 + num_1
    return m

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
