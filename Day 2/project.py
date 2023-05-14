# TIP CALCULATOR

print("Welcome to Tip Calculator")

# Get the total bill amount
total_bill = float(input("What was the total bill? "))

# Get the tip percentage
percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

# Convert tip to float value
percentage /= 100

# Get the tip amount
tip_amt = total_bill * percentage

# Calculate the total bill with the tip amount
total_bill += tip_amt

# Get the number of people for the split
split = int(input("How many people to split the bill? "))

# Calculate amount per person
pay_per_person = total_bill / split

# Print the value
print(round(pay_per_person,2))