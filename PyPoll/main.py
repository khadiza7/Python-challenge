#Import modules
import os
import csv

#Variable for total votes
votes_total = 0

#List of candidates
candidates = []

#Empty dictionary for storing the number of votes for each candidate
votes_for_candidates = {}

#Empty dictionary for storing vote percentage for each candidate
vote_percentage = {}

#Path to the data
election_path = os.path.join('election_data.csv')

#Read the file
with open(election_path, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #Stores the header
    csv_header = next (csvreader)

    #Loop through each row
    for row in csvreader:

        #Total number of votes
        votes_total += 1

        #List of candidates
        if row[2] not in candidates:
            candidates.append(str(row[2]))
        
        #Total number of votes for each candidate. 'in' scans all of the keys.
        #If candidate exists in the dictionry the vote will be added to the count.
        if row[2] in votes_for_candidates:
            votes_for_candidates[row[2]] += 1

            #If the candidate does not exist in the dictionary a new key will be added with a vote of 1.
            #dict[key] = [value] to add values.
        else:
            votes_for_candidates[row[2]] = 1

    #percentage of votes per candidate, three decimal places
    for candidate in votes_for_candidates:
        vote_percentage[candidate] = "{:0.3%}".format(votes_for_candidates[candidate] / votes_total)

    #Winner: Find the highest percentage of votes
    for candidate in vote_percentage:
        winnervalues = vote_percentage.values()
        maxvotes = max(winnervalues)
    
    #Find the candidate who is the winner
    for key,value in vote_percentage.items():
        if value == maxvotes:
            winner = key

#Merging dictionaries to add vote count to name and vote percentage
for a, b in vote_percentage.items():
        if a in votes_for_candidates.keys():
            votes_for_candidates[a] = [b,votes_for_candidates[a]]

#Print out the analysis
print("Election Results")
print("------------------------------------------")
print(f"Total votes: {votes_total}")
print("------------------------------------------")
for key,value in votes_for_candidates.items():
    print('%s:%s \n' % (key, value) )
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")

#Export the results to a text file
with open("Election.txt", "w") as Election:

    Election.write("Election Results\n")
    Election.write("------------------------------------------\n")
    Election.write(f"Total votes: {votes_total}\n")
    Election.write("------------------------------------------\n")

    for key,value in votes_for_candidates.items():
        Election.write('%s:%s \n' % (key, value) )

    Election.write("----------------------------\n")
    Election.write(f'Winner: {winner}\n' )
    Election.write("----------------------------\n")

    Election.close()