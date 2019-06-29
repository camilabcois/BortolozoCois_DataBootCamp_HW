import os
import csv
  
total_months = 0
net_total = 0
greatest_increase = 0
greatest_increase_month = ''
greatest_decrease = 0
greatest_decrease_month = ''
total_change = 0

#file to open
budget_path = os.path.join("Resources", "budget_data.csv")

with open(budget_path, newline='') as csvfile:

   
    csvreader = csv.reader(csvfile, delimiter=",")

    # converts csvreader to list
    rows_list = list(csvreader)

    #  for every row in the dataset
    for i in range(1, len(rows_list)):
       
        # add 1 to total_months
        total_months += 1

        # add in each row to the net_total
        net_total = net_total + int(rows_list [i][1])

        # calculate whether current row is max
        max_length_not_reached = i != len(rows_list) - 1

        if max_length_not_reached:
            total_change = total_change + int(rows_list[i + 1][1]) - int(rows_list[i][1])

            # increase
            if (greatest_increase < int(rows_list[i + 1][1]) - int(rows_list[i][1])):
                greatest_increase = int(rows_list[i + 1][1]) - int(rows_list[i][1])
                greatest_increase_month = rows_list[i + 1][0]

            # decrease
            if (greatest_decrease < int(rows_list[i][1]) - int(rows_list[i + 1][1])):
                greatest_decrease = int(rows_list[i + 1][1]) - int(rows_list[i][1])
                greatest_decrease_month = rows_list[i][0]


# prints results for the dataset to the terminal
def printResults():
    print('Financial Analysis')
    print('----------------------------')
    print('Total Months: ', total_months)
    print('Total: $', net_total)
    print('Average Change: $', round(abs(total_change) / (len(rows_list) - 1), 2))
    print('Greatest Increase in Profits: ', greatest_increase_month +  ' ($' + str (greatest_increase) + ')')
    print('Greatest Decrease in Profits: ', greatest_decrease_month +  ' ($-' + str (greatest_decrease) + ')')

#outputting results to a text file called Financial Analysis
def writeResults():
    output_file = "Financial_Analysis.txt"

    #open the output file
    file = open(output_file, 'w')

    #writing the rows to print in a text file
    file.write('Financial Analysis\n')
    file.write('----------------------------\n')
    file.write('Total_Months: ' + str(total_months) + '\n')
    file.write('Total : ' + str(net_total) + '\n')
    file.write('Average Change: $ ' + str(round(abs(total_change) / (len(rows_list) - 1), 2)) + '\n')
    file.write('Greatest Increase in Profits: ' + str(greatest_increase_month +  ' ($' + str (greatest_increase) + ')') + '\n')
    file.write('Greatest Decrease in Profits: ' + str(greatest_decrease_month +  ' ($-' + str (greatest_decrease) + ')') + '\n')
 

printResults()
writeResults()
   
    
    
    
    


