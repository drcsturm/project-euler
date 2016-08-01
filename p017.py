

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

w = {}
w[1] = 3
w[2] = 3
w[3] = 5
w[4] = 4
w[5] = 4
w[6] = 3
w[7] = 5
w[8] = 5
w[9] = 4
w[10] = 3
w[11] = 6
w[12] = 6
w[13] = 8
w[14] = 8
w[15] = 7
w[16] = 7
w[17] = 9
w[18] = 8
w[19] = 8
w[20] = 6
w[30] = 6
w[40] = 5
w[50] = 5
w[60] = 5
w[70] = 7
w[80] = 6
w[90] = 6
w[100] = w[1] + 10 # 10 = hundred and
w[200] = w[2] + 10
w[300] = w[3] + 10
w[400] = w[4] + 10
w[500] = w[5] + 10
w[600] = w[6] + 10
w[700] = w[7] + 10
w[800] = w[8] + 10
w[900] = w[9] + 10
w[1000] = 11

tens = 0
for i in range(1,10):
    tens += w[i]

one_to_nineteen = tens
for i in range(10,20):
    one_to_nineteen += w[i]

less_than_1hundred = one_to_nineteen
for i in range(20,100,10):
    less_than_1hundred += w[i]*10 + tens

total = less_than_1hundred + w[1000]
for i in range(100,1000,100):
    total += w[i]*100 + less_than_1hundred - 3 # remove the first and of the hundred section, e.g. one hundred = 100 which does not contain and

print(total)

