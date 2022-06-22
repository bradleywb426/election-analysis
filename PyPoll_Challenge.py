# Add our dependencies.
import csv
import os

# Defining load & save file variables
load = os.path.join("Resources", "election_results.csv")
save = os.path.join("analysis", "election_analysis.txt")

# Initialize total votes variable
total_votes = 0

# Defining CANDIDATE variables
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Defining COUNTY variables
county_list = []
county_votes = {}
largest_turnout = ""
largest_votes = 0


# Read the csv and convert it into a list of dictionaries
with open(load) as election_data:
    reader = csv.reader(election_data)
    # Read the header
    header = next(reader)
    # For each row in the CSV file.
    for row in reader:


        # Add to the total vote count
        total_votes = total_votes + 1
        # Extract CANDIDATE names
        candidate_name = row[2]
        # Extract COUNTY names
        county_name = row[1]


        # Check if CANDIDATE is in CANDIDATE list
        if candidate_name not in candidate_options:
            # Add unique CANDIDATE names to CANDIDATE list
            candidate_options.append(candidate_name)
            # And begin tracking that CANDIDATE's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that CANDIDATE's count
        candidate_votes[candidate_name] += 1


        # Check if COUNTY is in list of COUNTIES
        if county_name not in county_list:
            # Add unique COUNTIES to COUNTY list
            county_list.append(county_name)
            # Tracking votes per COUNTY
            county_votes[county_name] = 0
        # Adding votes to COUNTY
        county_votes[county_name] +=1


# Save the results to our text file.
with open(save, "w") as txt_file:


    # Election Results
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    # Print to Terminal
    print(election_results, end="")
    # Write to text file
    txt_file.write(election_results)


    # For loop to get COUNTY from dictionary
    for county_name in county_votes:
        # Get COUNTY vote count
        vote_counts = county_votes.get(county_name)
        # Calculate vote percentage per COUNTY
        county_percent = float(vote_counts)/float(total_votes)
         # COUNTY level results
        county_results = (
            f"{county_name}: {county_percent:.1%} ({vote_counts:,})\n")
        # Print to Terminal
        print(county_results)
        # Save to text file
        txt_file.write(county_results)
        # Determine winning COUNTY and its vote count
        if (vote_counts > largest_votes):
            largest_turnout = county_name
            largest_votes = vote_counts
            

    # COUNTY with largest turnout
    largest_county = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {largest_turnout}\n"
        f"--------------------\n")
    # Print to Terminal
    print(largest_county)
    # Save to text file
    txt_file.write(largest_county)


    # CANDIDATE results.
    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print to Terminal
        print(candidate_results)
        # Save to text file
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and CANDIDATE
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage


    # Winning CANDIDATE summary
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    # Print to Terminal
    print(winning_candidate_summary)
    # Save to text file
    txt_file.write(winning_candidate_summary)
