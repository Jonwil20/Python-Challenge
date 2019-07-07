
import os
import csv

budget_data = os.path.join("..", "Python_Stuff", "budget_data.csv")

with open(budget_data, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter = '.') 
        total_sum = sum(1 for line in open(budget_data)) - 1
with open(budget_data, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter = '.')
        total = sum(2 for line in open(budget_data)) - 1
        
        average = total/total_sum
        
        
print ('Financial Analysis')
print ('----------------------------')
print ('Total Months:', total)
print('Total:', total_sum)
print ('Average Change:', average)
print ('Greatest Increase in Profits: ', max(budget_data))
print ('Greatest Decrease in Profits: ', min(budget_data))        
