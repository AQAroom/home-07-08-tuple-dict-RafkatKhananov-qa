d = {}

password = input()
N = int(input())

for i in range(N):
    key, value = input().split()
    d[key] = value

has_digits = any(char.isdigit() for char in password)
has_upper_letter = any(char.isupper() for char in password)

if (len(password) >= int(d["мин_длина"])
        and has_digits
        and has_upper_letter):
    print("Да")
else:
    print("Нет")
