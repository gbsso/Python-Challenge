#%%
# PyBank
import os
import csv
# Files to load and output (Remember to change these)
file_to_load = os.path.join("Resources", "budget_data.csv")
file_to_output = os.path.join("analysis", "budget_analysis.txt")

# Declare Variables:
changes_by_month = []
list_of_months = []
number_of_months = 0
profit_losses = 0
greatest_decrease = 0
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease_month = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as budget_data:
   reader = csv.reader(budget_data)
   # Read the header
   header = next(reader)
   # For each row...
   for row in reader:



    # Setting variables for rows and calculating number 
    previous_row = int(row[1])
    number_of_months += 1
    profit_losses += int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]

    for row in reader:
           # Run the loader animation

         # Number of months:      
         number_of_months += 1
         # Determine profit and losses:
         profit_losses += int(row[1])

    # Difference between current month and previous month:

    Difference_between_months = int(row[1]) - previous_row
    changes_by_month.append(Difference_between_months)
    previous_row = int(row[1])
    list_of_months.append(row[0])

    # Determining the Greatest Increase:
    if int(row[1]) > greatest_increase:
        greatest_increase = int(row[1])
        greatest_increase_month = row[0]

     # Determining the Greatest Decrease:
    if int(row[1]) < greatest_decrease:
        greatest_decrease = int(row[1])
        greatest_decrease_month = row[0]   

    # Determining the Average:
    average_change = sum(changes_by_month)/ len(changes_by_month)

    decrease = min(changes_by_month)
    increase = max(changes_by_month)


# Print Analysis
 
# Print Analysis

financial_analysis = (f'''Financial Analysis"
---------------------------
Total Months: {number_of_months}
Total: ${profit_losses}
Average Change: ${average_change:.2f}")
Greatest Increase in Profits:, {greatest_increase_month}, (${increase})")
Greatest Decrease in Profits:, {greatest_decrease_month}, (${decrease})''')

#Print out analysis
print(financial_analysis)

#Create a .txt file containing the same analysis in the print out
analysis = open('financial_analysis.txt', 'w')

analysis.write(financial_analysis)

analysis.close()


 
    


