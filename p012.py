# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# Let us list the factors of the first seven triangle numbers:

#      1: 1
#      3: 1,3
#      6: 1,2,3,6
#     10: 1,2,5,10
#     15: 1,3,5,15
#     21: 1,3,7,21
#     28: 1,2,4,7,14,28

# We can see that 28 is the first triangle number to have over five divisors.

# What is the value of the first triangle number to have over five hundred divisors?

from utils.common import divisors

# # I read the problem wrong and solved for the smallest number with 500 divisors
# min_val = 14414400
# max_exp = 15
# for i23 in range(max_exp-5):
#     for i19 in range(max_exp-5):
#         for i17 in range(max_exp-5):
#             for i13 in range(max_exp-4):
#                 for i11 in range(max_exp-3):
#                     for i7 in range(max_exp-2):
#                         for i5 in range(max_exp-1):
#                             for i3 in range(max_exp):
#                                 for i2 in range(max_exp):
#                                     val = 2**i2 * 3**i3 * 5**i5 * 7**i7 * 11**i11 * 13**i13 * 17**i17 * 19**i19 * 23**i23
#                                     if val > min_val:continue
#                                     divisor_count = len(divisors(val))
#                                     if divisor_count >= 500:
#                                         min_val = min(min_val, val)
#                                         print(val, divisor_count, min_val, i2, i3, i5, i7, i11, i13, i17, i19, i23)

i = 0
val = 0
divisor_count = 0
while divisor_count < 500:
    i += 1
    val += i
    divisor_count = len(divisors(val))
    if i % 100 == 0:
        print(val, divisor_count)
print(val, divisor_count)
