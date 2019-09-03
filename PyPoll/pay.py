#import library
import os
import csv
import locale
locale.setlocale( locale.LC_ALL, '' )

# file path
file = "/Users/seve/UCBSF201908DATA2/01-Lesson-Plans/03-Python/Homework/PyPoll/Resources/election_data.csv"

# Declare Variables
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# Open csv in default read mode with context manager
with open(file,newline="", encoding="utf-8") as poll:

    # Store data under the csvreader variable
    csvreader = csv.reader(poll,delimiter=",")

    # Skip the header so we iterate through the actual values
    header = next(csvreader)

    # Iterate through each row in the csv
    for row in csvreader:

        # Count the unique Voter ID's and store in variable  called total_votes
        total_votes +=1

        # We have four candidates if the name is found, count the times it appears and store in a list
        # We can use this values in our percent vote calculation in the print statements
        if row[2] == "Khan":
            khan_votes +=1
        elif row[2] == "Correy":
            correy_votes +=1
        elif row[2] == "Li":
            li_votes +=1
        elif row[2] == "O'Tooley":
            otooley_votes +=1

 # To find the winner we want to make a dictionary out of the two lists we previously created
candidates = ["Khan", "Correy", "Li","O'Tooley"]
votes = [khan_votes, correy_votes,li_votes,otooley_votes]

# We zip them together the list of candidate(key) and the total votes(value)
# Return the winner using a max function of the dictionary
dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

# Print a the summary of the analysis
khan_percent = (khan_votes/total_votes) *100
khan = round(khan_percent)
correy_percent = (correy_votes/total_votes) * 100
correy= round(correy_percent)
li_percent = (li_votes/total_votes)* 100
li= round(li_percent)
otooley_percent = (otooley_votes/total_votes) * 100
otooley = round(otooley_percent)

# Print the summary table
print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Khan: {khan:.3f}% ({khan_votes})")
print(f"Correy: {correy:.3f}% ({correy_votes})")
print(f"Li: {li:.3f}% ({li_votes})")
print(f"O'Tooley: {otooley:.3f}% ({otooley_votes})")
print("----------------------------")
print("Winner: {key}")
print("----------------------------")

# Output files

#with open(output_file,"w") as file:
