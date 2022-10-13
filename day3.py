#Maurel ZODOGANHOU
#DAY3-DJANGO-CHALLENGE
print("💫💫💫WELCOME IN THIS PROGRAM WHICH CALCULATE A COMPOUND INTEREST FROM YOUR INPUT 💫💫💫")

original_amount = float(input("Enter your original amount : "))
annual_rate = float(input("Enter annuel interest rate in percent : "))
numberOfTime = float(input('Enter number of times per year interest is compounded : '))
numberOfYears = float(input('Enter number of years account will be left to earn interest : '))

final_amount  = (original_amount * (annual_rate / 100) / numberOfTime) * numberOfYears + original_amount
print ("Your final amount after" + str(numberOfYears) + " years is : " + str(final_amount))

