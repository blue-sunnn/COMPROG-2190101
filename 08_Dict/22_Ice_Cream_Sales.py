icecreams, topSale = {}, {}

for i in range(int(input())):
    name, price = input().split()
    icecreams[name] = price

for i in range(int(input())):
    name, sale = input().split()
    if name in icecreams:
        if name not in topSale:
            topSale[name] = int(sale) * int(icecreams[name])
        elif name in topSale:
            topSale[name] += int(sale) * int(icecreams[name])

val = topSale.values()
total = sum(val)

if total == 0:
    print('No ice cream sales')
else:
    m = max(val)
    print('Total ice cream sales: ' + str(float(total)))
    temp = sorted([[-sale, name] for name, sale in topSale.items()])
    topSale = [i[1] for i in temp if -i[0] == m]
    print('Top sales: ', end='')
    print(', '.join(topSale))
