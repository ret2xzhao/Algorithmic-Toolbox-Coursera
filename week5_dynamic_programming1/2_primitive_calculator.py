# Uses python3
import sys

# C(n) = min{1.if n % 3 = 0:C(n//3) + 1. 2.if n % 2 = 0:C(n//2) + 1. 3.else: C(n-1) + 1}

def optimal_sequence(n):
    sequence = []     
    operation_num = [0]*(n+1)
    operation_num[1] = 0
    for i in range(2, len(operation_num)):
        operation_num[i] = operation_num[i-1] + 1
        if i % 2 == 0:
            operation_num[i] = min(operation_num[i//2] + 1, operation_num[i])
        if i % 3 == 0:
            operation_num[i] = min(operation_num[i//3] + 1, operation_num[i])
    
    while n > 1:
        sequence.append(n)
        if operation_num[n-1] == operation_num[n]-1:
            n = n - 1
        elif (n % 2 == 0 and operation_num[n//2] == operation_num[n]-1):
            n = n//2     
        elif (n % 3 == 0 and operation_num[n//3] == operation_num[n]-1):
            n = n//3
    
    sequence.append(1)
    sequence.sort()
    return sequence

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
