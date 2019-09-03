#import library
import os
import csv


# file path
file = "election_data.csv"

# Declare Variables
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# open csv
with open(file,newline="", encoding="utf-8") as poll:
    csvreader = csv.reader(poll,delimiter=",")

# skip headers
    header = next(csvreader)

# Iterate through rows
    for row in csvreader:

# count  unique voters
        total_votes +=1

        if row[2] == "Khan":
            khan_votes +=1
        elif row[2] == "Correy":
            correy_votes +=1
        elif row[2] == "Li":
            li_votes +=1
        elif row[2] == "O'Tooley":
            otooley_votes +=1

 # to determine winner, combine two list via dictionary
candidates = ["Li", "Correy", "Khan","O'Tooley"]
votes = [li_votes, correy_votes,khan_votes,otooley_votes]


#using zip() to map values
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
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Khan: {khan:.3f}% ({khan_votes})")
print(f"Correy: {correy:.3f}% ({correy_votes})")
print(f"Li: {li:.3f}% ({li_votes})")
print(f"O'Tooley: {otooley:.3f}% ({otooley_votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")

# Output files

#output_main = "output_main.txt"
#with open(output_main,"w") as output:
    #output.write(summary_print)
