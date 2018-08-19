# creates a simple calculator that determines the price of a meal after tax and tip.

meal = 44.50
tax = 0.075
tip = 0.15

meal += meal * tax
total = meal + meal * tip
print(total)
