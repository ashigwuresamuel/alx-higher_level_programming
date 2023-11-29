#!/usr/bin/python3
number_dig = 0
while number_dig <= 89:
    if number_dig % 10 == 0:
        number_dig += 1 + number_dig // 10
    print("{:02d}".format(number_dig), end='\n' if number_dig == 89 else ", ")
    number_dig += 11
