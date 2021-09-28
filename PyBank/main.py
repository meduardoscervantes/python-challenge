#In this program we are taking the the CSV file in the folder
#and generating an output for a made up business.

import csv

#open and read the file to populate something that we can use to handle data
#use the data to find total months
#calculate the net profit/loss
#find the average +/-
#find the greatest increase in profits and print : {when, amount}
#find the greatest decrease in profits and print : {when, amount}



path = r'H:\2021 UTSA Bootcamp\HW_3_MESC\PyBank\Resources\budget_data.csv'
with open(path) as data:
        rawData = data.read()
        rows = rawData.split("\n")
        amount = []
        dates = []
        for i in range(2,len(rows)):
            temp = rows[i]
            dates.append(temp[:8])
            amount.append(temp[9:])
        
        print(dates)
        print(amount)
