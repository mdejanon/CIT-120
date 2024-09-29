# PROGRAM TITLE: WALL PAINTING COST CALCULATOR
# STUDENT: MAX DE JANON
# SECTION: 15889
# DATE: 03/ /2024


# Customer Wall Module: it collects the wall size (in square feet) data from the user.
def customer_wall():
    wall_size = float(input("Enter the square footage of the wall: "))
    return wall_size


# Customer Paint Module: it collects the cost of the paint (per gallon) from the user.
def customer_paint():
    paint_cost = float(input("Enter the cost of the paint per gallon: "))
    return paint_cost


# Paint Quantity Calculator Module: This module calculates the amount of paint
# needed for the wall size data collected from the user.
def paint_quantity_calculator(wall_size):
    paint_quantity = round(float(1 * (wall_size / 115)), 2)
    print(f"---------------------------------\nThe number of gallons of paint required: {paint_quantity}.")
    return paint_quantity


# Labor Time Calculator Module: This module calculates the labor time needed for
# the project using the wall size data collected from the user.
def labor_time_calculator(wall_size):
    labor_time = float(8 * (wall_size / 115))
    hrs_counter = labor_time
    hrs = 0
    while True:
        if hrs_counter >= 1:
            hrs_counter = hrs_counter - 1
            hrs = hrs + 1
        else:
            break
    mins = int(hrs_counter * 60)
    if mins != 0:
        print(f"The time of labor required: {hrs} hrs and {mins} mins.")
    else:    
        print(f"The hours of labor required: {hrs} hrs.")
    return labor_time


# Project Paint Cost Calculatro Module: This module calculated the cost of the pain for
# this project using the data calculated from the 'Paint Quantity Calculator Module' and
# the data collected from the 'Customer Paint Module'.
def ppc_calculator(paint_quantity, paint_cost_per_gallon):
    project_paint_cost = round(float(paint_cost_per_gallon * paint_quantity), 2) 
    print(f"The cost of the paint: ${project_paint_cost}.")
    return project_paint_cost


# Labor Cost Calculator Module: This module calculates the labor cost using the data
# from the 'Labor Time Calculator Module' and the cost per hour.
def labor_cost_calculator(labor_time):
    labor_cost = round(float(20 * labor_time), 2)
    print(f"The labor charges: ${labor_cost}.")
    return labor_cost


# Total Cost Calculator Module: This modile calculates the total cost of the project
# adding the data calculated from the 'Labor Cost Calculator Module' to the data
# from the 'Labor Cost Calculator Module'.
def total_cost_calculator(paint_project_cost, labor_cost):
    total_project_cost = round((paint_project_cost + labor_cost), 2)
    print(f"The total cost of the paint job: ${total_project_cost}.")


# Main Module: It calls for several modules that collect user data and do calculations.
def main():
    print("*** Wall Paint Cost Calculator***\n---------------------------------")
    wall_size = customer_wall()
    paint_cost_per_gallon = customer_paint()
    paint_quantity = paint_quantity_calculator(wall_size)
    labor_time = labor_time_calculator(wall_size)
    project_paint_cost = ppc_calculator(paint_quantity , paint_cost_per_gallon)
    labor_cost = labor_cost_calculator(labor_time)
    total_cost_calculator(project_paint_cost, labor_cost)
        
main()
