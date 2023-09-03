import datetime

username=input("what is your name")
# Display a greeting
print(f"Hello, {username}!")
year=input ("when were you born")
print(f"year of birth is, {year}!")

# Age is current year minus year of birth

current_year = datetime.datetime.now().year

print(f"The current year is: {current_year}")
