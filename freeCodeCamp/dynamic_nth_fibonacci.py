def fibonacci(n):
    if n == 0:
        return 0

    sequence = [0, 1]
    if n == 1:
        return 1

    for i in range(2, n + 1):
        next_val = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_val)

    return sequence[n]
