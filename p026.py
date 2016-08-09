

# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

#     1/2	= 	0.5
#     1/3	= 	0.(3)
#     1/4	= 	0.25
#     1/5	= 	0.2
#     1/6	= 	0.1(6)
#     1/7	= 	0.(142857)
#     1/8	= 	0.125
#     1/9	= 	0.(1)
#     1/10	= 	0.1 

# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

from decimal import *
getcontext().prec = 3000

max_len = 6
repeating = 6
repeating_num = 7
for n in range(6,1000):
	num = str(Decimal(1) / Decimal(n))[2:]
	if len(num) <= max_len * 2:continue
	for j in range(10):
		breaker = False
		for i in range(max_len, int(len(num)/2)-j):
			# print(n, num[j:j+i], num[j+i:i*2+j])
			if num[j:j+i] == num[j+i:i*2+j]:
				if len(num[j:i]) >= repeating:
					repeating = len(num[j:i])
					repeating_num = n
				# print(n, num[j:i])
				breaker = True
				break
		if breaker:break
print(repeating_num)
