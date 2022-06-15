#Load dependencies
import csv
import os

# create file load and save variables
load = os.path.join("Resources", "election_results.csv")
save = os.path.join("analysis", "election_analysis.txt")

#naming variables
total_votes = 0
candidates = []
votes_per = {}
winning_candidate = ""
winning_count = 0
winning_percent = 0

#loading data
with open(load) as data:

    #reading file
    file_read = csv.reader(data)

    #clearing header row
    headers = next(file_read)

    for row in file_read:
        total_votes += 1

        names = row[2]
        if names not in candidates:
            candidates.append(names)
            votes_per[names] = 0
        votes_per[names] += 1
for names in candidates:
    votes = votes_per[names]
    vote_percent = (float(votes)/float(total_votes))*100
    print(f"{names}: {vote_percent:.1f} ({votes:,})\n")
    
    if (votes>winning_count) and (vote_percent>winning_percent):
        winning_count = votes
        winning_percent = vote_percent
        winning_candidate = names
winner_summary = (
    f"----------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percent:.1f}\n")
print(winner_summary)