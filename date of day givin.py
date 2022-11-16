#this is the import of time and calender to make the programe work
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
#this just take the day from the calender DON'T TOUCH IT if you don't know what are you doing
#copy it if you need this part only
def findDay(date):
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday()
    return (calendar.day_name[born])
#that's the end of copying :)
#Its basicly jusr a day/month/year that written like that for example 10 09 2013
# the " " is just a space to separate between day, month and year
weekday = (day + " " + month + " " + year)
print("______________")
#findDay is basicly just finds the day of your givin date
#it's important too and in between () you type the variable
print("   " + findDay(weekday) + "   ")
print("______________")

