import math

def prime_list_below_num(max_num):
    # num = int(math.sqrt(max_num))
    potential_primes = list(range(3,max_num,2))
    num_loc = 2
    primes = [2,3,5]
    while num_loc < len(potential_primes):
        prime_num = True
        limit = math.sqrt(potential_primes[num_loc])
        for i in primes[1:]:
            if i > limit:
                break
            if potential_primes[num_loc] % i == 0:
                prime_num = False
        if prime_num:
            primes.append(potential_primes[num_loc])
        num_loc += 1
    return primes

if __name__ == '__main__':
    max_num = 1000
    plist = prime_list_below_num(max_num)
    print(plist)
