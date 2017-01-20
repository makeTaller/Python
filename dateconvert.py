
# dateconver.py
## Converts a date in form "mm/dd/yyyy" to "month, day, year"

def main():
    #get the date 
    #dateStr = input("Enter the date (mm/dd/yyyy): ")

    #get the day month and year
    day, month, year = eval(input("Enter day, month, and year numbers: "))

    date1 = str(month)+"/"+str(day)+"/"+str(year)


    #split into components
    #monthStr, dayStr, yearStr = dateStr.split("/")

    #convert monthStr to the month name
    months = ["January", "Febuary", "March", "April", "May",
              "June","July","August","September","October",
              "November", "December"]
    monthStr = months[int(monthStr)-1]

    date2 = monthStr+" " + ", " + str(year)

    print("The date is", date1, "or", date2+".")

    # output result in month day, year format
    #print("The converted date is:",type(monthStr), monthStr, dayStr + ",", yearStr)
main()
