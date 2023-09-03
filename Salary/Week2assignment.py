# Weeekly pay for newspaper carrier
# This Program will the carriers earnings

# test case

print("Carrier weekly Pay Calculator")
#prompt the number of papers delivered on the route per day
number_of_papers_per_day = int(input ("How many papers do you deliver on your route per day"))
print(f"you deliver,{number_of_papers_per_day}  papers per day ")
#prompt the number of days delivered per week

# prompt the user for the number of days the paper is delivered per week

number_of_day_per_week = int(input("How manys day(s) in a week do u deliver "))

print(f"you deliver,{number_of_day_per_week } days a week ")


#  prompt the user for the total amount of tips the carrir receives weeekly
amount_in_tips = float(input("How much do u receive in tips weekly"))

print(f" You Receive , a total amount of ${amount_in_tips } in tips weekly")


#  set and define constatnsts

cost_of_newspaper = 4.25
commmission = 0.1 # 10%


total_number_of_paper_delivered_weekly = number_of_papers_per_day * number_of_day_per_week

print(f" You deliver a total of {total_number_of_paper_delivered_weekly } newspapers  weekly")


# calculate weekly salary

total_weekly_sales = total_number_of_paper_delivered_weekly * cost_of_newspaper

weekly_salary = total_weekly_sales * commmission
formatted_weekly_salary = "{:.2f}".format(weekly_salary)
print(f"In a week you make ${formatted_weekly_salary} from the commission ")

total_weekly_pay = weekly_salary + amount_in_tips
formatted_total_weekly_pay = "{:.2f}".format(total_weekly_pay)
print(f"In a week you make a total of ${formatted_total_weekly_pay} from the commission and tips ")



















