import datetime
import calendar


#print datetime.datetime(1900, 1, 1).weekday()


count = 0

for year in range(1901,2001):
    for month in range(1,13):
        #for day in range(1, calendar.monthrange(year, month)+1):
        if datetime.datetime(year, month, 1).weekday() == 6:
            print (year, month, 1)
            count += 1
            

print count
