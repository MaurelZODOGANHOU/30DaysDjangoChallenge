#Maurel ZODOGANHOU
#DAY_7-DJANGO-CHALLENGE
#SLEEP DEBT CALCULATOR PROGRAM
print("Welcome! This program is a sleep debt calculator")
total_sleep_hour  = 0
required_sleep_hour = 8
total_sleep_debt = 0
i = 0
while(i != 8):
    sleep_debt = 0
    sleep_hour = 0
    sleep_hour = float(input(f" \n How many hours did you sleep the day {i} ?  "))
    sleep_debt += required_sleep_hour - sleep_hour
    total_sleep_hour += sleep_hour
    total_sleep_debt += sleep_debt
    i += 1
if(total_sleep_debt <= 0):
    print(f"You slept {total_sleep_hour} hours this week. You don't have any sleep debt!!!")
else: 
    print(f"You slept {total_sleep_hour} hours this week. you need more hours of sleep to be healthy ")

