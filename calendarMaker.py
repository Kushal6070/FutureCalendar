#import datetime module
import datetime


#Set the constants
MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July',
'August', 'September', 'October', 'November', 'December')

DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday',
'Friday', 'Saturday')


#ask user for the year by looping over
while True:
    print('Please enter a year: ')
    response = input('> ')

    if response.isdecimal() and 1<=len(response)<=4 :
        year = int(response)
        break
    
    print('Please enter a year like 2023:')
    continue

#ask user for the month
while True:
    print('Please enter month for the calendar, 1-12: ')
    response = input('>')

    if not response.isdecimal():
        print('Enter a numeric month, like 4 for April.')
        continue

    month = int(response)
    if 1<=month<=12:
        break

    print('Please enter a number from 1 to 12.')

#print the calendar intro
print('Welcome to the calendar maker by Kushal. Please enter the year and month you want to go to.')


#get calendar function
def getCalendar(year, month):
    #caltext will contain the string of the calendar
    calText = ''

    #Add the month and year at the top of calendar
    calText += (' '*34)+ MONTHS[month - 1]+ ' '+str(year)+'\n'

    #Add the days of the week to the calendar
    calText += '...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..\n'

    #The horizontal line string that seperate weeks:
    weekSeparator = ('+----------' * 7) + '+\n'

    #Days seperator with blank rows
    blankRow = ('|          ' * 7 + '|\n')

    #Getting the first date of the month with datetime module

    currentDate = datetime.date(year, month, 1)

    #Roll back currentdate until it is Sunday. 
    #weekday() returns 6 for Sunday, not 0

    while currentDate.weekday() != 6:
        currentDate -= datetime.timedelta(days=1)

    #loop over each week in month
    while True:
        calText += weekSeparator

        #dayNumberRow is the row with the day number labels:
        dayNumberRow = ''
        for i in range(7):
            dayNumberLabel = str(currentDate.day).rjust(2)
            dayNumberRow += '|' + dayNumberLabel + (''*8)
            currentDate += datetime.timedelta(days=1) #Goes to next day
        dayNumberRow += '|\n'

        #check if we're done with the month
        if currentDate.month != month:
            break

    #Add horizontal line at the bottom of the calendar
    calText += weekSeparator
    return calText

calText = getCalendar(year, month)
print(calText) #Display the calendar        

