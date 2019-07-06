# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    if capacity == 0:
            return value
    value_per_weight = [float(v) / float(w) for v, w in zip(values, weights)]
    for i in range(len(weights)):
        weight_max = max(value_per_weight)
        index = value_per_weight.index(weight_max)
        value_per_weight[index] = 0
        add_capacity = min(capacity, weights[index])
        value += add_capacity * weight_max
        weights[index] -= add_capacity
        capacity -= add_capacity
    return value

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
