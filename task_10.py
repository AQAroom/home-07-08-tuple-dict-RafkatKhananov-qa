d = {}

N = int(input())
for i in range(N):
    line_1 = input()
    key, value = line_1.split()
    d[key] = value

M = int(input())
for i in range(M):
    line_2 = input()
    key, value = line_2.split()
    d[key] = value

for key, value in d.items():
    print(f"{key}: {value}")
