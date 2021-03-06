

# Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten pentagonal numbers are:

# 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

# It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 − 22 = 48, is not pentagonal.

# Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk − Pj| is minimised; what is the value of D?

from utils.common import pentagonal, is_pentagonal

done = False
maxp = 10000
for j in range(1, maxp):
	for k in range(j+1, maxp):
		if is_pentagonal(pentagonal(k) - pentagonal(j)) and is_pentagonal(pentagonal(k) + pentagonal(j)):
			print(int(pentagonal(k) - pentagonal(j)))#, k, j)
			done = True
			break
	if done:break
