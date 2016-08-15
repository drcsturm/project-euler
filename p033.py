
# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

ans = 1
for i in range(10,100):
	if i%10 == 0:continue
	if i%11 == 0:continue
	for j in range(10,100):
		if j%10 == 0:continue
		if j%11 == 0:continue
		if j>=i:continue
		si = str(i)
		sj = str(j)
		for a in sj:
			if si.count(a) == 1:
				ni = int(si.replace(a,''))
				nj = int(sj.replace(a,''))
				if float(j/i) == float(nj/ni):
					# print(j,i,nj,ni,j/i)
					ans *= ni/nj
print(ans)
