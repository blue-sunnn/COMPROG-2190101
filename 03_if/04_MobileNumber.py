phone_num = ['06', '08', '09']

n = input()

if len(n) == 10 and n[0:2] in phone_num: print('Mobile number')
else: print('Not a mobile number')
