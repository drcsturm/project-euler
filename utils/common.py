# common routines

import math

def divisors(num):
    divisor_list = [1, num]
    i = 2
    if num >= i:
        while i not in divisor_list:
            if num % i == 0:
                divisor_list.append(i)
                divisor_list.append(int(num/i))
            i += 1
    return sorted(divisor_list)

if __name__ == "__main__":
    # print(len(divisors(100000000000000)))
    val = 2**5 * 3**4 * 5**3 * 7
    # print(divisors(val))
    print(val, len(divisors(val)))
