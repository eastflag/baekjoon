i = input().split(' ')
hour = int(i[0])
minute = int(i[1])
C = 45

minute -= C
if minute < 0:
    minute += 60
    hour -= 1
    if hour < 0:
        hour += 24
print('%d %d' %(hour, minute))
