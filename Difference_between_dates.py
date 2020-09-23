#difference between dates
from datetime import date
date1=date(2020,9,11)
date2=date(2020,8,19)
difference=date1-date2

#return number of days as an integer
print('DAYS: ',abs(difference.days))

#return number of weeks as an positive integer
print('WEEKS: ',abs(difference.days)//7)

'''
OUTPUT:
DAYS:  23
WEEKS:  3
'''