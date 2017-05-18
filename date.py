print('This program prints the day of ur birth')
import calendar
dy=int(input('Enter your day:'))
mth=int(input('Enter your month:'))
yr=int(input('Enter your year:'))
agie=calendar.weekday(yr,mth,dy)
nak={0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'}
print('Your day of birth is'),nak[agie]

