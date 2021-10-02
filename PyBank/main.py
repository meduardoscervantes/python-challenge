# In this program we are taking the the CSV file in the folder
# and generating an output for a made up business.
# open and read the file to populate something that we can use to handle data
# use the data to find total months
# calculate the net profit/loss
# find the average +/-
# find the greatest increase in profits and print : {when, amount}
# find the greatest decrease in profits and print : {when, amount}

# print to the console
import os

print("Financial Analysis")
print("----------------------------")
# open the data stream
path = r'resources\budget_data.csv'
with open(path) as data:
    # create local variables and read the raw data into a string
    rawData = data.read()
    # split the data by lines into rows
    rows = rawData.split("\n")
    mTotal = 0
    amount = []
    dates = []
    differences = []
    header = rows[0].split(',')
    # separate the data into its respective categories
    for i in range(1, len(rows) - 1):
        temp = rows[i]
        # @Note - I could have seperated the data into two with the str.split(',')
        #         but i found it more fun to use substrings.
        dates.append(temp[:8])
        amount.append(int(temp[9:]))
    print(f"Total Months: {len(dates)}")
    # print the total to the console
    print(f"Total: ${sum(amount)}")
    mTotal = 0
    # parse the information to find the difference between each month
    for x in range(1, len(amount)):
        differences.append(int(amount[x]) - int(amount[x-1]))
    # print to the console the average of all differences
    print(f"Average Change: {round(sum(differences)/len(differences),2)}")
    # declare local variable to find the lowest and highest difference
    low = 0
    high = 0
    posLow = 0
    posHigh = 0
    # parse through the differences and find the max and min differences
    for x in range(len(differences)):
        if differences[x] < low:
            low = differences[x]
            posLow = x
        if differences[x] > high:
            high = differences[x]
            posHigh = x
    # print the output to the console
    print(f"Greatest Increase in Profits: {dates[posHigh + 1]} ({high})")
    print(f"Greatest Decrease in Profits: {dates[posLow + 1]} ({low})")
    # create a new directory inside PyBank and the output.txt file and write all the information
    os.mkdir("analysis")
    os.chdir("analysis")
    f = open("PyBank_output.txt", "a")
    f.write("Financial Analysis")
    f.write(f"\n----------------------------")
    f.write(f"\nTotal Months: {len(dates)}")
    f.write(f"\nTotal: ${sum(amount)}")
    f.write(f"\nAverage Change: {round(sum(differences)/len(differences),2)}")
    f.write(f"\nGreatest Increase in Profits: {dates[posHigh + 1]} ({high})")
    f.write(f"\nGreatest Decrease in Profits: {dates[posLow + 1]} ({low})")
    # close the file streams.
    f.close()
    data.close()