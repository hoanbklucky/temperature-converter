#ask user for a positive integer number
import time

#ask for a postive integer number from user
number = int(input('enter a positive integer number: '))
#count down loop
while number > 0:
    print(number)
    time.sleep(1)
    number  = number - 1

print('Happy New Year')