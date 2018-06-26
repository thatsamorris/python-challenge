import csv

months = []
revenue = []
with open('./budgetdata.CSV') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        months.append(row[0])
        revenue.append(row[1])

total_months = len(months[1:])
#init vars 
net_revenue = 0
largest_increase = revenue[1]
largest_decrease = revenue[1]
for amount in revenue[1:]:
    if amount >= largest_increase:
        largest_increase = amount
    elif amount < largest_decrease:
        largest_decrease = amount

    net_revenue += int(amount)
#reopened csv to look for largesat and smallest increase. 
with open('./budgetdata.CSV') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        if largest_increase in row:
            top_month = row
        elif largest_decrease in row:
            bottom_month = row
average_change = round((net_revenue / total_months), 2)

with open('./pybanktxt.txt', 'w') as writefile:
    writefile.writelines('Financial Analysis\n')
    writefile.writelines('----------------------------' + '\n')
    writefile.writelines('Total Months: ' + str(total_months) + '\n')
    writefile.writelines('Total Revenue: $' + str(net_revenue) + '\n')
    writefile.writelines('Average Change: $' + str(average_change) + '\n')
    writefile.writelines('Greatest Increase in Revenue: ' + str(top_month[0]) + ' ' + str('(' + top_month[1] + ')') + '\n')
    writefile.writelines('Greatest Decrease in Revenue: ' + str(bottom_month[0]) + ' ' + str('(' + top_month[1] + ')') + '\n')

with open('pybanktxt.txt', 'r') as readfile:
    print(readfile.read())