
import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

#Declare variables required for assignment
count = 0
total = 0
GValue = -float('inf')
GDValue = float('inf')
previous_profit_losses = float('inf')
GValue_date = None
GDValue_date = None
sum_change = 0

#Open csv path as file
with open(csvpath) as csvfile:
    handle = csv.reader(csvfile, delimiter=",")
    next(handle) # to skip header
    
# Read through each row of data after the header
    for row in handle:
        date, profit_losses = row
        count = count + 1
        total = total + int(profit_losses)
     
    #Logic for determining mean, greatest increase/decrease in profits 
        if count > 1:
            Difference = int(profit_losses) - int(previous_profit_losses)
            sum_change = sum_change + Difference
            
            if Difference > GValue:
                GValue = Difference
                GValue_date = date

            if Difference < GDValue:
                GDValue = Difference
                GDValue_date = date
        
        previous_profit_losses = profit_losses 

#Logic for Average Change
Avg_change = round(sum_change/(count - 1),2)

#Print output in required format
output_str = f'''Financial Analysis
----------------------------
Total Months: {count}
Total: ${total}
Average Change: ${Avg_change}
Greatest Increase in Profits: {GValue_date} (${GValue})
Greatest Decrease in Profits: {GDValue_date} (${GDValue})
'''

print(output_str)

# Export/save output_str to text file
Outputpath = os.path.join('Analysis', 'Financial analysis.txt')
text_file = open (outputpath, "w")
n = text_file.write(output_str)
text_file.close() 
