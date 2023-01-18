import os
import csv

csvpath = os.path.join('Resources','election_data.csv')

#Declare variables required for assignment
votes_count = 0
DD = {}

#Open csv path as file
with open(csvpath) as csvfile:
    handle = csv.reader(csvfile, delimiter=",")
    next(handle) # to skip header

#Logic for counting Total Votes
    for row in handle:
        ballot_ID, County, Candidate  = row
        votes_count = votes_count + 1

        if Candidate not in DD:
            DD[Candidate] = 0
        DD[Candidate] = DD[Candidate] + 1

#Logic for determining winner with the highest vote count and percentage
string2 = ""

for Candidate,votes in DD.items():
    string2 = string2 + f"{Candidate}: {round(votes/votes_count*100, 3)}% ({votes})\n"

# winner logic
winner_candidate = None
max_votes = 0

for name,vote in DD.items():
    if vote > max_votes:
        winner_candidate = name
        max_votes = vote

#Print output in required format
output_string = f'''Election Results
-------------------------
Total Votes: {votes_count}
-------------------------
{string2} -------------------------
Winner: {winner_candidate}
-------------------------
'''

print (output_string)

# Export/save output_str to text file
csvpath = os.path.join('Analysis','ElectionResults.txt')
with open(csvpath, 'w') as f:
    f.write(output_string)