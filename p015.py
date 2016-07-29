# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20×20 grid?

import numpy as np
np.set_printoptions(linewidth=240)


# size is the number of complete square on one dimension
# for example a size of 2 would consist of 3x3 dots to make a total of 4 squares
size = 20
z = np.zeros((size+1,size+1), dtype=np.int64)
z[0,:] = 1
z[:,0] = 1

for i in range(1,size+1):
    for j in range(1,size+1):
        z[i,j] = z[i-1,j] + z[i,j-1]
print(z[size,size])
print(np.rot90(np.rot90(z)))
