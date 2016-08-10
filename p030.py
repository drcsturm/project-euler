

# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

#     1634 = 1**4 + 6**4 + 3**4 + 4**4
#     8208 = 8**4 + 2**4 + 0**4 + 8**4
#     9474 = 9**4 + 4**4 + 7**4 + 4**4

# As 1 = 14 is not a sum it is not included.

# The sum of these numbers is 1634 + 8208 + 9474 = 19316.

# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

found = []
for n in range(2, 200000): # anything over 1000000 will be too large, from trial and error 200000 is large enough
	ns = str(n)
	ns_t = 0
	for i in ns:
		ns_t += int(i)**5
	if ns_t == n:
		# print(n)
		found.append(n)
# print(found)
print(sum(found))
