#import library
import os
import csv
import locale

# file path
file = "PyBank.csv"

# create empty lists to iterate through rows
total_months = []
net_total_profit = []
monthly_profit_change = []

# open csv in default read mode with context manager
with open(file,newline="", encoding="utf-8") as bank:
    csvreader = csv.reader(bank,delimiter=",")

# skip the headers
    header = next(csvreader)

# iterate through the rows in csv
    for row in csvreader:

# append
        total_months.append(row[0])
        net_total_profit.append(int(row[1]))

# iterate through the profits to caclulate monthly change
    for x in range(len(net_total_profit)-1):

# take the difference and append
        monthly_profit_change.append(net_total_profit[x+1]-net_total_profit[x])

# get max and min
max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)

# correlate max and min
max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1


# print output

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(net_total_profit)}")
print("----------------------------")
print(f"Average Change: ${round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")
print("----------------------------")


#with open(output_file,"w") as file:

#output_main = "output_main.txt"
#with open(output_main,"w") as output:
    #output.write(summary_print)
