number = input('Input a number,press Enter to quit >>>')
nMax = 0
while number:
    if nMax < int(number):
        nMax = int(number)
    number = input('Input a number ,presss endter to quit >>>')
else:
    print('the max value {} '.format(nMax))
