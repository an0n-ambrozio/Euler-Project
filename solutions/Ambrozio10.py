# Answer: 142913828922 
# Problem 10: Summation of primes
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

def solve():
    limit = 2000000
    sieve = [True] * limit
    sieve[0] = sieve[1] = False
    
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, limit, i):
                sieve[j] = False
                
    prime_sum = 0
    for i in range(limit):
        if sieve[i]:
            prime_sum += i
            
    print(prime_sum)

if __name__ == "__main__":
    solve()
