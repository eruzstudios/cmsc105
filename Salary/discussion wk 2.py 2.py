# This program calculates revenue earned from sales of laptops on ebay.
# It prompts the user for the number of units sold and the price per unit,
# applies a tax rate, and displays the total revenue.
# Value for the tax rate 
TAX_RATE = 0.08

# Prompt the user for the number of units sold which is 30
units_sold = int(input("Enter the number of units sold: "))

# Prompt the user for the price per unit which is 300
price_per_unit = float(input("Enter the price per unit: "))

# Calculate the total revenue before tax
total_revenue = units_sold * price_per_unit

# Calculate the tax amount
tax_amount = total_revenue * TAX_RATE

# Calculate the total revenue after tax
total_revenue_after_tax = total_revenue - tax_amount

# Display the results
print(f"Total Revenue (before tax): ${total_revenue:.2f}")
print(f"Tax Amount: ${tax_amount:.2f}")
print(f"Total Revenue (after tax): ${total_revenue_after_tax:.2f}")
