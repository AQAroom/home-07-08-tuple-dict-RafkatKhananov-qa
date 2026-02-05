d = {}

while True:
    line = input()
    if line == "":
        break
    subject, grade = line.split()
    d[subject] = int(grade)

count = 0
total = 0

for i in d.values():
    count += 1
    total += i

print(f"{total / count:.2f}")
