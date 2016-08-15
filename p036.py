

# The decimal number, 585 = 1001001001(base2) (binary), is palindromic in both bases.

# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

# (Please note that the palindromic number, in either base, may not include leading zeros.)

ans = 0
for i in range(1000000):
	b = bin(i)[2:]
	if str(i) == str(i)[::-1] and b == b[::-1]:
		# print(i)
		ans += i
print(ans)