# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

import csv
import os
#Assign a variable for the file to load an the path.
file_to_load = os.path.join("Election_Analysis","election_results.csv")
#Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Election_Analysis", "analysis", "election_analysis.txt")

#1. Initialize a total vote counter
total_votes=0

#Create a new list of candidates
candidate_options = []

#Create a new dictionary of candidate votes
candidate_votes = {}

#Declare a variable for the winning candidate
winning_candidate = ""

#Declare a variable for the "winning count" equal to zero
winning_count = 0

#Declare a variable for the "winning_percentage" equal to zero
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_results:

    # To do: perform analysis.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_results)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        #Add to the total vote count
        total_votes += 1
        # Print the candidate name from each row
        candidate_name = row[2]
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            #Set candidates vote to zero
            candidate_votes[candidate_name] = 0
        #Tally candidate votes
        candidate_votes[candidate_name] += 1

with open(file_to_save, "w") as txt_file:
    election_results = (
        f"Election Results\n"
        f"----------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"----------------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)
# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # 4. Print the candidate name and percentage of votes.
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
        
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)

