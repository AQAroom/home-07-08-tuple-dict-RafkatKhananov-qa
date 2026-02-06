d = {}

N = int(input())
for i in range(N):
    line = input()
    key, value = line.split()
    d[key] = value

M = int(input())
for i in range(M):
    line = input()
    key, value = line.split()
    d[key] = value

print(d)
