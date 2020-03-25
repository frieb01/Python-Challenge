#import the csv file plumbing
import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #skips header
    csv_header = next(csvreader)

    #initialize all my variables
    first_row = []
    monthly_diff_list = []
    monthly_differences = 0

    #store the first row in variables
    first_row = next(csvreader)
    first_month = first_row[0]
    previous_amount = int(first_row[1])
    net_total = previous_amount

    #add first row to lists
    month_list = [first_month]
    monthly_diff_list = [0]
    
    # Read each row of data after the header & first row
    for row in csvreader:

        #put dates into list
        month_list.append(row[0])

        #add all the profit/loss figures together
        profit_loss = int(row[1])
        net_total = net_total + profit_loss

        #subtract the previous month each time, accumulate the difference and create a list with it
        monthly_differences = monthly_differences + (int(row[1])-previous_amount)
        monthly_diff_list.append(int(row[1])-previous_amount)

        #redefine the previous amount before going to the next row
        previous_amount = int(row[1])


#make final calculaions and pull final numbers
greatest_increase = max(monthly_diff_list)
greatest_increase_month = month_list[monthly_diff_list.index(greatest_increase)]
greatest_decrease = min(monthly_diff_list)
greatest_decrease_month = month_list[monthly_diff_list.index(greatest_decrease)]
total_months = len(month_list)
average_change = monthly_differences/(total_months-1)

#print everything
print("Total Months: " + str(total_months))
print("Net Total: $" + str(net_total))
print(f'Average Change: $ {average_change:.2f}')
print(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})')
print(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})')

#write the results to a text file
output_path = os.path.join("Output", "new.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the lines to rows
    csvwriter.writerow(["Total Months: " + str(total_months)])
    csvwriter.writerow(["Net Total: $" + str(net_total)])
    csvwriter.writerow([f'Average Change: $ {average_change:.2f}'])
    csvwriter.writerow([f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})'])
    csvwriter.writerow([f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})'])
