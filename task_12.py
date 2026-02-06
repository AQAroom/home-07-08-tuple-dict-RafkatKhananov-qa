d = {}

while True:
    city = input()
    if city == "":
        break
    if city not in d:
        d[city] = 1
    else:
        d[city] += 1

for city, count in sorted(d.items()):
    print(f"{city}: {count}")
