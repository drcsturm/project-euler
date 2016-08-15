

# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

# How many circular primes are there below one million?

from utils.primes import is_prime, primesfrom2to
plist = primesfrom2to(1000000)
ans = [2,3,5,]
for p in plist:
	if p in ans:continue
	add_num = True
	potential = []
	sp = list(str(p))
	if '2' in sp or '4' in sp or '5' in sp or '6' in sp or '8' in sp:continue
	for s in [[sp[i - j] for i in range(len(sp))] for j in range(len(sp))]:
		v = int(''.join(s))
		if v in potential:continue
		if v in plist:
			potential.append(v)
		else:
			add_num = False
			break
	if add_num:
		# print(potential)
		ans += potential
# print(ans)
print(len(ans))