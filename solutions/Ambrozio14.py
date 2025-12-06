# Problem 14: Longest Collatz sequence
# Which starting number, under one million, produces the longest chain?

memo = {}

def collatz_length(n):
    if n == 1:
        return 1
    if n in memo:
        return memo[n]
    if n % 2 == 0:
        next_n = n // 2
    else:
        next_n = 3 * n + 1
    length = 1 + collatz_length(next_n)
    memo[n] = length
    return length

max_length = 0
max_start = 0
for i in range(1, 1000000):
    length = collatz_length(i)
    if length > max_length:
        max_length = length
        max_start = i

print(max_start)