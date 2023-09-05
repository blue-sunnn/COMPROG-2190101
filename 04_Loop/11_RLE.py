s = input()
count = 1

for i in range(1, len(s)) :
  if s[i] == s[i - 1] :
    count += 1
  else :
    print(s[i - 1], count, end = ' ')
    count = 1

print(s[len(s) - 1], count)