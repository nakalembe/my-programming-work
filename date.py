print('this program prints the day of ur birth')
import calendar
dy=int(input('enter ur day:'))
mth=int(input('enter ur month:'))
yr=int(input('enter ur year:'))
sar=calendar.weekday(yr,mth,dy)
aher={0:'monday',1:'tuesday',2:'wednesday',3:'thursday',4:'friday',5:'saturday',6:'sunday'}
print'ur day of birth is',aher[sar]

