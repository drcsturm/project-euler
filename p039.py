

# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

# {20,48,52}, {24,45,51}, {30,40,50}

# For which value of p ≤ 1000, is the number of solutions maximised?

ans = 0
max_count = 0
for p in range(1, 1001):
	count = 0
	for a in range(1, 1000):
		if a >= p:continue
		b = (p**2 - 2*p*a)/2/(p-a) # solving for b from a+b+c=p and a**2+b**2=c**2
		if b % 1 == 0:
			count += 1
	if count >= max_count:
		max_count = count
		ans = p
print(ans)