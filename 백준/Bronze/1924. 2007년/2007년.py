import datetime
x,y = map(int,input().split())


time1 = datetime.date(2007,x,y)
time1.weekday()

week = {0:'MON',1:'TUE',2:'WED',3:'THU',4:'FRI',5:'SAT',6:'SUN'}

print(week[time1.weekday()])