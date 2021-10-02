# This program will look at the data provided in the .csv file and then display:
# total number of votes, list of candidates who received votes, percentage of votes with number,
# and the winner of the election
import os
print("Election Results")
print("-------------------------")
path = "resources/election_data.csv"
with open(path) as data:
    # Read data and declare local variables
    rawData = data.read()
    voterId = []
    candidate = []
    county = []
    tallyVotes = dict()
    wName = "NA"
    wVal = 0
    # separate the data based on the break next line
    rows = rawData.split("\n")
    # save the header
    header = rows[0].split(',')
    # parse through the data starting after the headers until 1 minus the end because the data has an empty final row
    for i in range(1, len(rows) - 1):
        # split each row upon the ','
        temp = rows[i].split(',')
        # separate the rows into their respective array
        for j in range(len(temp)):
            if j == 0:
                voterId.append(temp[j])
            if j == 1:
                county.append(temp[j])
            if j == 2:
                candidate.append(temp[j])
    # create directory and the output.txt file and start outputting info for the console and separate file
    os.mkdir("analysis")
    os.chdir("analysis")
    f = open("PyPoll_Output.txt", "a")
    print(f"Total Votes: {len(voterId)}")
    print("-------------------------")
    f.write("Election Results")
    f.write("\n-------------------------")
    f.write(f"\nTotal Votes: {len(voterId)}")
    f.write("\n-------------------------")
    # count the total votes for each respective candidate
    for i in candidate:
        if i in tallyVotes:
            tallyVotes[i] += 1
        else:
            tallyVotes[i] = 1
    # output the final total results to the console and the .txt file
    for i in tallyVotes:
        print(f"{i}: {round((tallyVotes.get(i) / len(candidate)) * 100, 4) }% ({tallyVotes.get(i)})")
        f.write(f"\n{i}: {round((tallyVotes.get(i) / len(candidate)) * 100, 4) }% ({tallyVotes.get(i)})")
        #find who is the winner
        if tallyVotes[i] > wVal:
            wName = i
            wVal = tallyVotes[i]
    # output the final total results to the console and the .txt file
    print("-------------------------")
    print(f"Winner: {wName}")
    print("-------------------------")
    f.write("\n-------------------------")
    f.write(f"\nWinner: {wName}")
    f.write("\n-------------------------")
    # close out the file streams
    f.close()
    data.close()