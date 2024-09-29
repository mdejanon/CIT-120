# STUDENT: Max De Janon
# CLASS: CIT-12000
# SECTION: 15889
# DATE: 01/25/2024

# Ask the user to enter the price of 4 items.
item1 = float(input("Enter the price of the first item: "))
item2 = float(input("Enter the price of the second item: "))
item3 = float(input("Enter the price of the third item: "))
item4 = float(input("Enter the price of the fourth item: "))

# Calculate the sub total by adding all the items.
subTotal = item1 + item2 + item3 + item4

# Calculate the sales tax at a rate of 6%.
salesTax = subTotal * 0.06

# Calculate the total.
total = subTotal + salesTax

# Display the sub total, sales tax and total values.
print (f"The sub total is : ${subTotal}")
print (f"The sales tax is : ${salesTax}")
print (f"The total is : ${total}")
