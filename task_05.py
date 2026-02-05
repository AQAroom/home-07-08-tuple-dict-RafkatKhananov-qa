hours = int(input())
minutes = int(input())
seconds = int(input())

time = (hours, minutes, seconds)

print(time[0] * 3600 + time[1] * 60 + time[2])
