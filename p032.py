
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

divs = []
for i in range(2, 9876):
	si = ''.join(sorted(str(i)))
	if '0' in si:continue
	add_num = True
	for j in si:
		if si.count(j) > 1:
			add_num = False
			break
	if add_num:
		divs.append(i)

ans = []
for i in divs:
	top = int(i**0.5)+1
	for j in divs:
		if j > top:break
		if i%j == 0:
			num = ''.join(sorted(str(i) + str(j) + str(i//j)))
			if num == '123456789':
				# print([j, i//j, i])
				ans.append(i)
				break
print(sum(ans))
