month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

n = input().split('/')

n[1] = int(n[1]) - 1

print(month_list[n[1]] + ' ' + n[0] + ',' + ' ' + n[2])