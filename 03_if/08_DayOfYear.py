dl = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

d = int(input())
m = int(input())
y = int(input()) - 543  # change from B.E. to A.D.

# check leap year
if y % 400 == 0: dl[1] += 1
elif y % 4 == 0 and y % 100 != 0: dl[1] += 1

print(sum(dl[:m - 1]) + d)
