# common routines

import math

def divisors(num, proper=True):
    divisor_list = [1]
    if not proper:
        divisor_list.append(num)
    i = 2
    if num >= i:
        while i not in divisor_list and i <= num/2:
            if num % i == 0:
                divisor_list.append(i)
                if int(num/i) != i:
                    divisor_list.append(int(num/i))
            i += 1
    return sorted(divisor_list)


def pandigital(num, start=1, end=9):
    pannum = [str(i) for i in range(start, end+1)]
    if pannum == sorted(str(num)):
        return True
    else:
        return False


def read_words(filename):
    with open(filename) as f:
        raw_text = f.readline()
    return [w for w in raw_text.replace('"',"").split(",")]


if __name__ == "__main__":
    # print(len(divisors(100000000000000)))
    val = 2**5 * 3**4 * 5**3 * 7
    # print(divisors(val))
    print(val, len(divisors(val)))
