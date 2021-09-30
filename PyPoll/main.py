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
    khanVotes = 0
    correyVotes = 0
    liVotes = 0
    tooleyVotes = 0
    winner = 0
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
    print(f"Total Votes: {len(voterId)}")
    print("-------------------------")
    for i in range(len(candidate)):
        if candidate[i] == "Khan":
            khanVotes += 1
        elif candidate[i] == "Correy":
            correyVotes += 1
        elif candidate[i] == "Li":
            liVotes += 1
        elif candidate[i] == "O'Tooley":
            tooleyVotes += 1
    print(f"Khan: {round(khanVotes/len(candidate)*100,4)}% ({khanVotes})")
    print(f"Correy: {round(correyVotes/len(candidate)*100,4)}% ({correyVotes})")
    print(f"Li: {round(liVotes/len(candidate)*100,4)}% ({liVotes})")
    print(f"O'Tooley: {round(tooleyVotes/len(candidate)*100,4)}% ({tooleyVotes})")
    print("-------------------------")
    print("Winner: Khan")
    print("-------------------------")
    f = open("PyPoll_Output.txt", "a")
    f.write("Election Results")
    f.write("\n-------------------------")
    f.write(f"\nTotal Votes: {len(voterId)}")
    f.write("\n-------------------------")
    f.write(f"\nKhan: {round(khanVotes/len(candidate)*100,4)}% ({khanVotes})")
    f.write(f"\nCorrey: {round(correyVotes/len(candidate)*100,4)}% ({correyVotes})")
    f.write(f"\nLi: {round(liVotes/len(candidate)*100,4)}% ({liVotes})")
    f.write(f"\nO'Tooley: {round(tooleyVotes/len(candidate)*100,4)}% ({tooleyVotes})")
    f.write("\n-------------------------")
    f.write("\nWinner: Khan")
    f.write("\n-------------------------")
    f.close()
    data.close()