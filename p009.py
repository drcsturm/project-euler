# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

## a2 + b2 = c2 and a + b + c = 1000 so a+b+sqrt(a2+b2)=1000

import math
for a in range(1,501):
    for b in range(1,501):
        if a + b + math.sqrt(a**2 + b**2) == 1000:
            aa = a
            bb = b
c = 1000 - aa - bb
# print(aa,bb,c)
print(aa*bb*c)

