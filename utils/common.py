# common routines

import math

def triangle(n):
    return n * (n + 1) / 2

def is_triangle(n):
    return ((8 * n + 1)**0.5 - 1) / 2 % 1 == 0

def pentagonal(n):
    return n * (3 * n - 1) / 2

def is_pentagonal(n):
    if n <= 0:return False
    return ((24 * n + 1)**0.5 + 1) / 6 % 1 == 0

def hexagonal(n):
    return n * (2 * n - 1)

def is_hexagonal(n):
    return ((8 * n + 1)**0.5 + 1) / 4 % 1 == 0

def is_quadratic(n, q_type=None, a=None, b=None, c=None):
    if not q_type and (a is None or b is None or c is None):return False
    if q_type == 'triangle':a=1;b=1;c=-2
    if q_type == 'pentagonal':a=3;b=-1;c=-2
    if q_type == 'hexagonal':a=2;b=-1;c=-1
    if a is None or b is None or c is None:return False
    return ((-4*a*c * n + b**2)**0.5 + 1) / 2*a % 1 == 0 or ((-4*a*c * n + b**2)**0.5 - 1) / 2*a % 1 == 0

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
