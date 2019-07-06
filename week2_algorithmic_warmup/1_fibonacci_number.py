# Uses python3
# def calc_fib(n):
#     if (n <= 1):
#         return n
# 
#     return calc_fib(n - 1) + calc_fib(n - 2)
# 
# n = int(input())
# print(calc_fib(n))

def calc_fib(n):
    if (n <= 1):
        return n
    previous = 0
    current = 1
    for i in range(2,n+1):
        new = previous + current
        previous = current
        current = new
    return new

n = int(input())
print(calc_fib(n))
