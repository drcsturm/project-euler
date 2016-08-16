

# An irrational decimal fraction is created by concatenating the positive integers:

# 0.12345678910_1_112131415161718192021...

# It can be seen that the 12th digit of the fractional part is 1.

# If dn represents the nth digit of the fractional part, find the value of the following expression.

# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
d = ''
l = 1
ans = 1
for i in range(300000):
	d += str(i)
	if len(d) > l:
		# print(d[l])
		ans *= int(d[l])
		l *= 10
print(ans)