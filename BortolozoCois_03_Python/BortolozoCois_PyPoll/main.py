import os
import csv
  
candidates = []
all_votes = []


#output results to a text file called Poll Results
output_file = "Poll_Results.txt"
#open the output file
file = open(output_file, 'w')


def printResults():
    winner_count = 0
    total_votes = len(rows_list) - 1
    winners_output = ''

    print('Election Results')
    print('----------------------------')
    print('Total Votes: ', total_votes)
    print('----------------------------')

    for can in candidates:
        candidate_count = all_votes.count(can)
        winners_output = winners_output + can + ': '  + str( round((candidate_count / total_votes) * 100, 1) ) + '% (' + str(candidate_count) + ')' + '\n'
        print(can + ': ' + str( round((candidate_count / total_votes) * 100, 1) ) + '% (' + str(candidate_count) + ')')

        if candidate_count > winner_count:
            winner_count = candidate_count
            winner = can

    print('----------------------------')
    print('Winner : ' + winner)
    print('----------------------------')

    file.write('Election Results\n')
    file.write('----------------------------\n')
    file.write("Total Votes: " + str(total_votes) + '\n')
    file.write('----------------------------\n')
    file.write(winners_output)
    file.write('----------------------------\n')
    file.write('Winner : ' + winner + '\n')
    file.write('----------------------------\n')

election_path = os.path.join('Resources', 'election_data.csv')
with open(election_path, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    # converts csvreader to list
    rows_list = list(csvreader)

    # A complete list of candidates who received votes: get the list of voters in col 3, position 2
    # Print the contents of each row
    for i in range(1, len(rows_list)):
        # if candidate no in candidates list
        if rows_list[i][2] not in candidates:
            # add candidate to candidates list
            candidates.append(rows_list[i][2])

        # add each candidate to all_votes list
        all_votes.append(rows_list[i][2])

printResults()



    


