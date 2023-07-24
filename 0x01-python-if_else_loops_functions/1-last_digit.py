#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num_str = repr(number)
last_dig_str = num_str[-1]
last_dig = int(last_dig_str)

if last_dig > 5:
    print('Last digit of', number, 'is', last_dig, 'and is greater than 5')
elif last_dig == 0:
    print('Last digit of', number, 'is', last_dig, 'and is 0')
else:
    print('Last digit of', number, 'is', last_dig,
            'and is less than 6 and not 0')
