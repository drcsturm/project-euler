# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

from utils.primes import prime_list_below_num

plist = prime_list_below_num(200000)
print(plist[10000])