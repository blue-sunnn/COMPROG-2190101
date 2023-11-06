temp1, temp2 = set(), set()
for i in range(int(input())):
    x = set(input().split())
    if i == 0:
        temp1 = x
        temp2 = x
    else:
        temp1 = temp1.union(x)
        temp2 = temp2.intersection(x)

print(len(temp1))
print(len(temp2))
