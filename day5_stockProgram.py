#Maurel ZODOGANHOU
#DAY5-DJANGO-CHALLENGE
#STOCK TRANSACTION PROGRAM

num_share = 2000          # Number of shares
per_share_before = 40     # Value of each share when he purchased
commission_rate = 0.03    # Commission rate for stockbroker
per_share_after = 42.75   # Value of each share when sells
commission1 = per_share_before * num_share * commission_rate # Commission when Joe buys
commission2 = per_share_after * num_share * commission_rate  # Commission when Joe sells
profit =  ((per_share_after - per_share_before) * 2000) - (commission1 + commission2) #profit made by Joe

print("The amount of money Joe paid for the stock is $", num_share * per_share_before, sep="") #sep="" used for good display
print("\nThe amount of commission Joe paid his broker when he bought the stock is $", 
      num_share * per_share_before * commission_rate, sep="")
print("\nThe amount that Joe sold the stock for is $", num_share * per_share_after, sep="")
print("\nThe amount of commission Joe paid his broker when he sold the stock is $",
      num_share * per_share_after * commission_rate, sep="")

if (profit > 0) :
    print("\nAfter doing his business, Joe has made $"+str(profit)+" profit of money.\n")
else :
    print("\nAfter doing his business, Joe has lost $"+str(profit)+" amount of money\n")
