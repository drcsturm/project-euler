

# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

from utils.primes import is_prime, primesfrom2to
plist = primesfrom2to(1000000)
ans = []
for p in plist:
	if p < 10:continue
	sp = list(str(p))
	add_num = True
	for s in [sp[:i] for i in range(1,len(sp))] + [sp[i+1:] for i in range(len(sp)-1)]:
		v = int(''.join(s))
		if v not in plist:
			add_num = False
			break
	if add_num:
		# print(p)
		ans.append(p)
		if len(ans) == 11:break
print(sum(ans))
