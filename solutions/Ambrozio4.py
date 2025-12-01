# Answer: 906609
# Problem 4: Largest palindrome product
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def solve():
    max_palindrome = 0
    for i in range(999, 99, -1):
        for j in range(999, i - 1, -1):
            product = i * j
            if product <= max_palindrome:
                break 
            if str(product) == str(product)[::-1]:
                max_palindrome = product
    return max_palindrome

if __name__ == "__main__":
    print(solve())
