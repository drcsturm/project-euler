# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def palindrome(s):
    return s == s[::-1]

max_palindrome = 0
for i in range(999,100,-1):
    for j in range(999,100,-1):
        if palindrome(str(i * j)):
            if i*j > max_palindrome:
                print(i, j, i * j)
                max_palindrome = i * j
print(max_palindrome)
