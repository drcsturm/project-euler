

# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

# 9 = 7 + 2×1**2
# 15 = 7 + 2×2**2
# 21 = 3 + 2×3**2
# 25 = 7 + 2×3**2
# 27 = 19 + 2×2**2
# 33 = 31 + 2×1**2

# It turns out that the conjecture was false.

# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

from utils.primes import primesfrom2to, is_prime
num = 1
while True:
	found = False
	num += 2
	if is_prime(num):continue
	pl = primesfrom2to(num)
	for p in pl:
		for i in range(1, int(((num - p) / 2)**0.5) + 1):
			if num == p + 2 * i**2:
				found = True
				break
		if found:
			break
	if not found:
		print(num)
		break
