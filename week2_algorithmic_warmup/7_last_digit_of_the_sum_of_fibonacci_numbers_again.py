# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

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

# Fm + Fm+1 + … + Fn = F(n+2) — F(m+1)

def fibonacci_partial_sum(from_, to):
    return ((get_fibonacci_huge(to+2, 10) +10) - (get_fibonacci_huge(from_+1, 10) +10)) % 10

if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum(from_, to))
