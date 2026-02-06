d = {}

text = input()

for i in text:
  if "a" <= i <= "z":
    if i in d:
      d[i] += 1
    else:
      d[i] = 1

print(d)
