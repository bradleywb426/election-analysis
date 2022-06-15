#Load dependencies
import csv
import os

# create file load and save variables
load = os.path.join("Resources", "election_results.csv")
save = os.path.join("analysis", "election_analysis.txt")

#defining variables
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

    #header row
    headers = next(file_read)
    for row in file_read:

        #adding to total vote count
        total_votes += 1

        #getting candidate names
        names = row[2]

        if names not in candidates:
            
            #copying each unique name
            candidates.append(names)

            #tallying votes per candidate
            votes_per[names] = 0
        votes_per[names] += 1

#saving data
with open(save, "w") as txt_file:

    election_results = (
        f"\nElection Results\n"
        f"--------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"--------------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)

    for names in candidates:

        #getting & printing results for each candidate
        votes = votes_per[names]
        vote_percent = (float(votes)/float(total_votes))*100
        #print(f"{names}: {vote_percent:.1f}% ({votes:,})\n")
        candidate_results = (f"{names}: {vote_percent:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
        
        #finding the winner + data
        if (votes>winning_count) and (vote_percent>winning_percent):
            winning_count = votes
            winning_percent = vote_percent
            winning_candidate = names

    #printing winner data
    winner_summary = (
        f"----------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percent:.1f}\n")
    txt_file.write(winner_summary)
    #print(winner_summary)