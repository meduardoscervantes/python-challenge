# This program will look at the data provided in the .csv file and then display:
# total number of votes, list of candidates who received votes, percentage of votes with number,
# and the winner of the election
print("Election Results")
print("-------------------------")
path = "resources/election_data.csv"
with open(path) as data:
    rawData = data.read()
    voterId = []
    candidate = []
    county = []
    tallyVotes = dict()
    wName = "NA"
    wVal = 0
    rows = rawData.split("\n")
    for i in range(1, len(rows) - 1):
        temp = rows[i].split(',')
        for j in range(len(temp)):
            if j == 0:
                voterId.append(temp[j])
            if j == 1:
                county.append(temp[j])
            if j == 2:
                candidate.append(temp[j])
    f = open("PyPoll_Output.txt", "a")
    print(f"Total Votes: {len(voterId)}")
    print("-------------------------")
    f.write("Election Results")
    f.write("\n-------------------------")
    f.write(f"\nTotal Votes: {len(voterId)}")
    f.write("\n-------------------------")
    for i in candidate:
        if i in tallyVotes:
            tallyVotes[i] += 1
        else:
            tallyVotes[i] = 1
    for i in tallyVotes:
        print(f"{i}: {round((tallyVotes.get(i) / len(candidate)) * 100, 4) }% ({tallyVotes.get(i)})")
        f.write(f"\n{i}: {round((tallyVotes.get(i) / len(candidate)) * 100, 4) }% ({tallyVotes.get(i)})")
        if tallyVotes[i] > wVal:
            wName = i
            wVal = tallyVotes[i]
    print("-------------------------")
    print(f"Winner: {wName}")
    print("-------------------------")
    f.write("\n-------------------------")
    f.write(f"\nWinner: {wName}")
    f.write("\n-------------------------")
    f.close()
    data.close()