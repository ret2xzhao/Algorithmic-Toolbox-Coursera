# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10

def get_fibonacci(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current

def Pisano_period_length(m):
    previous = 0
    current = 1
    for i in range(m * m):
        #previous, current = current, (previous + current) % m
        temp = previous
        previous = current
        current = (temp + current) % m
        if previous == 0 and current == 1:
            return i + 1

def get_fibonacci_huge(n, m):
    remainder = n % Pisano_period_length(m)
    return get_fibonacci(remainder) % m

# Sum of Fib(1) + Fib(2) + ... + Fib(n) = Fib(n+2) - 1

def fibonacci_sum_last_digit(n):
    return (get_fibonacci_huge(n+2, 10) -1) % 10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_last_digit(n))
