icecreams, topSale = {}, {}

for i in range(int(input())):
    name, price = input().split()
    icecreams[name] = price

for i in range(int(input())):
    name, sale = input().split()
    if name in icecreams:
        if name not in topSale:
            topSale[name] = int(sale) * int(icecreams[name])
        else:
            topSale[name] += int(sale) * int(icecreams[name])

total = sum(topSale.values())

if total == 0:
    print('No ice cream sales')
else:
    m = max(topSale.values())
    print('Total ice cream sales: ' + str(float(total)))
    temp = sorted([[-sale, name] for name, sale in topSale.items()])
    topSale1 = [i[1] for i in temp if -i[0] == m]
    print('Top sales: ' + ', '.join(topSale1))
