import csv
import os

# create file load and save variables
load = os.path.join("Resources", "election_results.csv")
save = os.path.join("analysis", "election_analysis.txt")
with open(load) as data:

    file_read = csv.reader(data)
    headers = next(file_read)
    print(headers)
    for row in file_read:
        print(row)

    # Data
    # Total number of votes cast
    # A complete list of candidates who received votes
    # Total number of votes each candidate received
    # Percentage of votes each candidate won
    # The winner of the election based on popular vote

 




with open(save, "w") as outfile:
    outfile.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson\n")
    outfile.write("Arapahoe, Denver, Jefferson, ")