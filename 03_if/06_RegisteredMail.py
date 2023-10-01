n = int(input())

if n > 2000: print('Reject')
elif 1000 < n <= 2000: print(str(58))
elif 500 < n <= 1000: print(str(38))
elif 250 < n <= 500: print(str(28))
elif 100 < n <= 250: print(str(22))
else: print(str(18))
