d = {}

while True:
    line = input()
    if line == "":
        break
    good, price = line.split()
    d[good] = int(price)

max_key = max(d, key=d.get)
print(max_key)
