r = int(input())
g = int(input())
b = int(input())

rgb = (r, g, b)

if (rgb[0] == rgb[1]
    and rgb[1] == rgb[2]
    and rgb[1] == rgb[2]):
    print("Да")
else:
    print("Нет")
