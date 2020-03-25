#import the csv file plumbing
import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

candidates_list = []

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #skips header
    csv_header = next(csvreader)
    
    #write each row of column 3 to a list
    for row in csvreader:
        candidates_list.append(row[2])

#initialize dictionary
candidates_dict ={}

#loop through list to create a dictionary and update values based on name
for row in candidates_list:
    if row not in candidates_dict:
        candidates_dict[row] = 1
    else:
        candidates_dict[row] += 1

#get numbers for calculations
total_votes = int(len(candidates_list))
winner = max(candidates_dict, key=candidates_dict.get)

#print to terminal
print("Election Results")
print("-------------------------")
print (f'Total Votes: {total_votes}')
print("-------------------------")
for candidate in candidates_dict:
    print(f'{candidate}: {candidates_dict[candidate]/total_votes*100:.3f}% ({candidates_dict[candidate]})')
print("-------------------------")
print(f'Winner: {winner}')
print("-------------------------")

#write the results to a text file
output_path = os.path.join("Output", "new.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    #Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the results to rows
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow([f'Total Votes: {total_votes}'])
    csvwriter.writerow(["-------------------------"])
    for candidate in candidates_dict:
        csvwriter.writerow([f'{candidate}: {candidates_dict[candidate]/total_votes*100:.3f}% ({candidates_dict[candidate]})'])
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow([f'Winner: {winner}'])
    csvwriter.writerow(["-------------------------"])