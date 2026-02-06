d_1 = {}
d_2 = {}

N = int(input())
for i in range(N):
    key, value = input().split()
    d_1[key] = value

M = int(input())
for i in range(M):
    key, value = input().split()
    d_2[key] = value

for key in sorted(d_1):
    print(f"{key}: {d_1[key]}")

for key in sorted(d_2):
    print(f"{key}: {d_2[key]}")
