
# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
import numpy as np
from utils.common import divisors
max_num = 28123
abundant_nums = np.zeros(max_num, dtype=np.int8)
for i in range(12, max_num):
    if sum(divisors(i, proper=True)) > i:
        abundant_nums[i] = 1
# print(np.bincount(abundant_nums))

nums = np.ones(max_num, dtype=np.int8)
for i in range(24, max_num):
    for a in range(12, i//2 + 1):
        if abundant_nums[a] == 0:continue
        if abundant_nums[i-a] == 1:
            # this is the sum of two abundant numbers so remove from list by setting to 0
            nums[i] = 0
            break
num_sum = 0
for i, n in enumerate(nums):
    if n == 1:
        num_sum += i
print(num_sum)
