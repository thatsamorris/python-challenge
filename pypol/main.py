import csv

#assign empty list variables and append each voter id to list by searching rows for canidate name
total_voters = []
votes_for_Khan = []
votes_for_Correy = []
votes_for_Li = []
votes_for_Otooley = []

#open csv file containing data set and use for loop to search rows
with open('./election_data.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        total_voters.append(row[0])
        if 'Khan' in row:
            votes_for_Khan.append(row[0])
        elif 'Correy' in row:
            votes_for_Correy.append(row[0])
        elif 'Li' in row: 
            votes_for_Li.append(row[0])
        else: 
            votes_for_Otooley.append(row[0])

#integer variables for total votes and votes recieved by each canidate
total_votes = len(total_voters) - 1
total_Khan = len(votes_for_Khan)
total_Correy = len(votes_for_Correy)
total_Li = len(votes_for_Li)
total_Otooley = len(votes_for_Otooley) - 1

#convert votes into percentages

percent_Khan = round((total_Khan/total_votes) * 100 , 3)
percent_Correy = round((total_Correy/total_votes) * 100 , 3)
percent_Li = round((total_Li/total_votes) * 100 , 3)
percent_Otooley = round((total_Otooley/total_votes) * 100 , 3)

# assign percentages to dictionary to pass into winner function
dict_of_percentages = {percent_Khan: 'Khan' , percent_Correy: 'Correy' , percent_Li : 'Li', percent_Otooley: "O'tooley"}

#define function to determine winner
def winner(list_of_percentages):
    for percent in list_of_percentages:
        if percent == max(list_of_percentages):
            maxpercent = percent
            winner = list_of_percentages[maxpercent]
    return winner

#print statments of election results to txt file
with open('./pypoltxt.txt', 'w') as writefile:
    writefile.writelines('Election Result\n')
    writefile.writelines('-------------------------\n')  
    writefile.writelines('Total Votes: ' + str(total_votes) + '\n')
    writefile.writelines('-------------------------\n')
    writefile.writelines('Khan: ' + str(percent_Khan) + '% (' + str(total_Khan) + ')\n')
    writefile.writelines('Correy: ' + str(percent_Correy) + '% (' + str(total_Correy) + ')\n')
    writefile.writelines('Li: ' + str(percent_Li) + '% (' + str(total_Li) + ')\n')
    writefile.writelines("O'Tooley: " + str(percent_Otooley) + '% (' + str(total_Otooley) + ')\n')
    writefile.writelines('-------------------------\n')
    writefile.writelines('Winner: ' + winner(dict_of_percentages) + '\n')
    writefile.writelines('-------------------------\n')

with open('pypoltxt.txt', 'r') as readfile:
    print(readfile.read())