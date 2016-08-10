
# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

# It can be verified that the sum of the numbers on the diagonals is 101.

# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

import numpy as np
np.set_printoptions(linewidth=240)

size = 1001
z = np.empty((size, size), dtype=np.int64)

count = 1
row = size//2
col = size//2
loc = 0
z[row, col] = 1
while True:
	loc += 1
	for i in range(loc):
		count += 1
		if col+i+1 == size:break
		z[row, col+i+1] = count
	col += loc
	if col == size:
		break
	for i in range(loc):
		count += 1
		z[row+i+1, col] = count
	row += loc

	loc += 1
	for i in range(loc):
		count += 1
		z[row, col-i-1] = count
	col -= loc
	for i in range(loc):
		count += 1
		z[row-i-1, col] = count
	row -= loc
print(np.sum(np.diagonal(z)) + np.sum(np.diagonal(np.rot90(z))) - 1)