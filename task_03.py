x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

t1 = (x1, y1)
t2 = (x2, y2)

print(f"{((t2[0] - t1[0]) ** 2 + (t2[1] - t1[1]) ** 2) ** 0.5:.2f}")
