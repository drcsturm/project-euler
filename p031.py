

# In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

#     1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

# It is possible to make £2 in the following way:

#     1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

# How many different ways can £2 be made using any number of coins?

count = 0
for p200 in range(0, 201, 200):
	for p100 in range(0, 201, 100):
		if p100 + p200 > 200:break
		for p50 in range(0, 201, 50):
			if p50 + p100 + p200 > 200:break
			for p20 in range(0, 201, 20):
				if p20 + p50 + p100 + p200 > 200:break
				for p10 in range(0, 201, 10):
					if p10 + p20 + p50 + p100 + p200 > 200:break
					for p5 in range(0, 201, 5):
						if p5 + p10 + p20 + p50 + p100 + p200 > 200:break
						for p2 in range(0, 201, 2):
							if p2 + p5 + p10 + p20 + p50 + p100 + p200 > 200:break
							for p1 in range(201):
								if p1 + p2 + p5 + p10 + p20 + p50 + p100 + p200 == 200:
									# print(p1, p2//2, p5//5, p10//10, p20//20, p50//50, p100//100, p200//200)
									count += 1
								if p1 + p2 + p5 + p10 + p20 + p50 + p100 + p200 > 200:break
print(count)
