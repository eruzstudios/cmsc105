#made to find total cost of Computer and accessories plus tax
#user is asked how much computer is
#user is asked how many accessories


    
taxrate= .08

#welcome and promotional
print("Welcome to Micah's computer store!")
print("This system was designed to help you find out your total")
print("Today we have a deal where every accessory you buy with a Computer is only $5 per accessory")
      
#prompt for Computer price
computerprice= int(input("\nWhat is the price of your Computer? $ \t    "))

#prompt for ammount of accessories
accessories= int(input("How many accessories are you wanting to purchase? \t    "))

#calculate cost of accessories
accescost= accessories * 5

#calculate accessories total to computer price
total= accescost + computerprice

#calculate Tax of total
tax= taxrate * total

#calculate total of fullprice and tax
fullcost= tax+ total

#Displaying full total
print(" Your total is: $ ",fullcost)

# Prompt for the price of the extra cable
cable_price = int(input("What is the price of the extra cable? $ "))

# Add the cost of the extra cable to the full cost
fullcost += cable_price

# Display the updated total
print("Your updated total with the extra cable is: $", fullcost)