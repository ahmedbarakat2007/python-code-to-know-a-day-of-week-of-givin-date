import datetime
import calendar

print ("___________________")
print ("   Enter the day   ")
print ("___________________")
day = input ()
print ("_____________________")
print ("   Enter the month   ")
print ("_____________________")
month = input ()
print ("____________________")
print ("   Enter the year   ")
print ("____________________")
year = input ()

def findDay(date):
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday()
    return (calendar.day_name[born])
weekday = (day + " " + month + " " + year)
print("______________")
print("   " + findDay(weekday) + "   ")
print("______________")

