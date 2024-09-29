# PROGRAM TITLE: SHIPPING COST CALCULATOR
# STUDENT: MAX DE JANON
# SECTION: 15889
# DATE: 02/11/2024


# Ask the user to enter the weight of the package.
packageWeight = float(input("Welcome to The Fast Freight Shipping Company!\nEnter the weight of the package: "))

# Calculates the shipping cost depending on the weight of the package and the rates per pound.
if packageWeight > 0:
    if packageWeight > 0 and packageWeight <= 2:
        shippingCost = round(packageWeight * 1.10, 2)
        if not packageWeight >= 1:
            packageOunceWeight = round(float(packageWeight * 16), 2)
            packageGramWeight = round(float(packageOunceWeight * 28), 2)
            shippingCentCost = int(shippingCost * 100)
            if packageOunceWeight >= 1:
                if shippingCost >= 1:
                    print(f"The rate per pound is $1.10 for your {packageOunceWeight} Ozs package.\nThe shipping cost is: ${shippingCost}.")
                else:
                    print(f"The rate per pound is $1.10 for your {packageOunceWeight} Ozs package.\nThe shipping cost is: ¢{shippingCentCost}.")
            else:
                if shippingCost >= 0.01:
                    print(f"The rate per pound is $1.10 for your {packageGramWeight} grams package.\nThe shipping cost is: ¢{shippingCentCost}.")
                else:
                    print(f"The rate per pound is $1.10 for your {packageGramWeight} grams package.\nYour package is too small, the minimum shipping cost is: ¢1.")
        else:
            print(f"The rate per pound is $1.10 for your {packageWeight} lbs package.\nThe shipping cost is: ${shippingCost}.")
    if packageWeight > 2 and packageWeight <= 6:
        shippingCost = round(packageWeight * 2.20, 2)
        print(f"The rate per pound is $2.20 for your {packageWeight} lbs package.\nThe shipping cost is: ${shippingCost}.")
    if packageWeight > 6 and packageWeight <= 10:
        shippingCost = round(packageWeight * 3.70, 2)
        print(f"The rate per pound is $3.70 for your {packageWeight} lbs package.\nThe shipping cost is: ${shippingCost}.")
    if packageWeight > 10:
        shippingCost = round(packageWeight * 3.80, 2)
        print(f"The rate per pound is $3.80 for your {packageWeight} lbs package.\nThe shipping cost is: ${shippingCost}.")
else:
    print(f"ERROR: Package weight cannot be 0lbs.")
