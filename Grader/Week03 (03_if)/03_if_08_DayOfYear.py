day_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

d = int(input())
m = int(input())
y = int(input()) - 543

# check leap year
if y % 400 == 0:                   day_in_months[1] += 1
elif y % 4 == 0 and y % 100 != 0:  day_in_months[1] += 1

print(sum(day_in_months[:m - 1]) + d)
