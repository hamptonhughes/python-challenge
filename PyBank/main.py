#import modules

import os
import csv

#set file path for our csv file

csvpath = os.path.join("Resources", "budget_data.csv")

#open csv file and define the csv reader, start reading on line after header

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader, None)

#define month sum and profits and set them to 0 to be used in for loop

    monthsum=0
    profits=0

#create lists that we will be appending to
    CurrentMonth=[]
    month = []

 #for loop to read through csv file   
    for row in csvreader:

#add 1 to monthsum and profits for each time we loop thru 
        monthsum = monthsum + 1
        profits = profits + int(row[1])
    
#create two lists for columns 1 and 2
        CurrentMonth.append(row[1])
        month.append(row[0])
    
#remove first first row and last row from the two comparison months with list comprehension

    IntCurrent = [int(i) for i in CurrentMonth [1:]]
    IntPrevious = [int(j) for j in CurrentMonth [:-1]]
    nextmonth = [k for k in month [1:]]

#create a new list for the difference between current and previous months

    difference = [x - y for x, y in zip(IntCurrent, IntPrevious)]
    difference_total = 0

#create a function that finds the average monthly change

    def Average(difference):
        return round(sum(difference) / len(difference),2)
    mean_difference = round((Average(difference)),2)

#find the max monthly change
    maxdiff = difference[0]
    for c,d in zip(nextmonth,difference):
        if d > maxdiff:
            maxdiff = d
            maxmonth = c
        elif d == maxdiff:
            maxdiff = d


#find the min monthly change

    mindiff = difference[0]
    for c,d in zip(nextmonth,difference):
        if d < mindiff:
            mindiff = d
            minmonth = c
        elif d == mindiff:
            mindiff = d
#print it out

    print(f"Financial Analysis")
    
    print(f"_______________________________________________________________________________")
    
    print(f"Total Months: {monthsum}")

    print(f"Total: ${profits}")
    print(f"Average Change: ${mean_difference}")
    print(f"Greatest Increase in profits: {maxmonth} (${maxdiff})")
    print(f"Greatest Increase in profits: {minmonth} (${mindiff})")

#set file path for summary file
summary = os.path.join('Analysis','summary.txt')
#print to text file

lines = [f"Financial Analysis",f"_______________________________________________________________________________",f"Total Months: {monthsum}",f"Total: ${profits}",f"Average Change: ${mean_difference}",f"Greatest Increase in profits: {maxmonth} (${maxdiff})",f"Greatest Increase in profits: {minmonth} (${mindiff})"]
with open(summary, 'w') as text:
    text.write('\n'.join(lines))
    
    text.close()