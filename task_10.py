d = {}

N = int(input())
for i in range(N):
    key, value = input().split()
    d[key] = value

M = int(input())
for i in range(M):
    key, value = input().split()
    d[key] = value

for key in sorted(d):
    print(f"{key}: {d[key]}")
