import datetime 
  
# datetime(year, month, day, hour, minute, second) 
time1 = datetime.datetime.now()
time2 = datetime.datetime(2018, 6, 30, 8, 21, 10) 
  
# returns a timedelta object 
c = time1-time2
print('Difference: ', c) 
  
minutes = c.total_seconds() / 60
print('Total difference in Minutes: ', minutes) 
  
# returns the difference of the time of the day 
minutes = c.seconds / 60
print('Difference in Minutes: ', minutes) 

years = c.days / 365.25
print('Difference in Years', years)