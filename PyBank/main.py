# In this program we are taking the the CSV file in the folder
# and generating an output for a made up business.
# open and read the file to populate something that we can use to handle data
# use the data to find total months
# calculate the net profit/loss
# find the average +/-
# find the greatest increase in profits and print : {when, amount}
# find the greatest decrease in profits and print : {when, amount}

print("Financial Analysis")
print("----------------------------")
path = r'resources\budget_data.csv'
with open(path) as data:
    rawData = data.read()
    rows = rawData.split("\n")
    mTotal = 0
    amount = []
    dates = []
    differences = []
    # seperate the data into its respective categories
    for i in range(1, len(rows) - 1):
        temp = rows[i]
        dates.append(temp[:8])
        amount.append(temp[9:])
    print(f"Total Months: {len(dates)}")
    # find the total
    for x in amount:
        mTotal += int(x)
    print(f"Total: ${mTotal}")
    mTotal = 0
    for x in range(1, len(amount)):
        differences.append(int(amount[x]) - int(amount[x-1]))
    for x in range(len(differences)):
        mTotal += differences[x]
    print(f"Average Change: {round(mTotal/len(differences),2)}")
    low = 0
    high = 0
    posLow = 0
    posHigh = 0
    for x in range(len(differences)):
        if differences[x] < low:
            low = differences[x]
            posLow = x
        if differences[x] > high:
            high = differences[x]
            posHigh = x
    print(f"Greatest Increase in Profits: {dates[posHigh + 1]} ({high})")
    print(f"Greatest Decrease in Profits: {dates[posLow + 1]} ({low})")
    f = open("PyBank_output.txt", "a")
    f.write("Financial Analysis")
    f.write(f"\n----------------------------")
    f.write(f"\nTotal Months: {len(dates)}")
    f.write(f"\nTotal: ${mTotal}")
    f.write(f"\nAverage Change: {round(mTotal/len(differences),2)}")
    f.write(f"\nGreatest Increase in Profits: {dates[posHigh + 1]} ({high})")
    f.write(f"\nGreatest Decrease in Profits: {dates[posLow + 1]} ({low})")
    f.close()
    data.close()