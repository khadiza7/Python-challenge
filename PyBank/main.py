import os
import csv

#Variable to store the results
months = []
net_total = []
profit_change = []

#Path to the data
csv_path = os.path.join('budget_data.csv')

#Read the file
with open(csv_path, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #Stores the header
    csv_header = next (csvreader)

#Loop through each row, add each month and each profit/loss to their respective lists.
    for row in csvreader:
        months.append(row[0])
        net_total.append(int(row[1]))

 
#Calculate number of months by finding the length of the months list
total_month = (len(months))

#Calculate the net total of profit/losses by summing the list
total_net = sum(net_total)

#Change in profit/loss between each month (-1 as there are only 85 calculations required)
#[x+1] - [x] is the next month minus the previous month to find the change
for x in range(len(net_total)-1):
        profit_change.append(net_total[x+1] - net_total[x])

#Average change in profit/loss
average_change = sum(profit_change) / len(profit_change)

#Greatest increase in profits (date and amount) over entire period
#+1 is required as the index will show the previous month
increase = max(profit_change)
date_max = profit_change.index(increase)+1


#Greatest decrease in profits (date and amount) over entire period
#+1 is required as the index will show the previous month
decrease = min(profit_change)
date_min = profit_change.index(decrease)+1

#Print out the Analysis
print("Financial Analysis")
print("----------------------------------------------------------")
print(f"Total Months: {total_month}")
print(f"Total: ${total_net}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {months[date_max]} (${increase})")
print(f"Greatest Decrease in Profits: {months[date_min]} (${decrease})")


#Write a text file of the results, note: 'write' used instead of 'writerow' for text file.
with open("Analysis.txt", "w") as Analysis:
    Analysis.write("Financial Analysis\n")
    Analysis.write("-----------------------------------\n")
    Analysis.write(f"Total Months:{total_month}\n")
    Analysis.write(f"Total: ${total_net}\n")
    Analysis.write(f"Average Change: ${average_change}\n")
    Analysis.write(f"Greatest Increase in Profits: {months[date_max]} (${increase})\n")
    Analysis.write(f"Greatest Decrease in Profits: {months[date_min]} (${decrease})\n")

    Analysis.close()
