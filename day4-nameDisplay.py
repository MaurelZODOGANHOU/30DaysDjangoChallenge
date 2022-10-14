#Maurel ZODOGANHOU
#DAY4-DJANGO-CHALLENGE
firstName = str(input("Enter your first name:  "))
lastName = str(input("Enter your last name : "))
initials = firstName[0].title() + "." + lastName[0].upper()
adress_book = firstName.title() + " " + lastName.upper()
username = firstName[0].lower()+lastName.lower()   
print("Initials  : " + initials)
print("Adress book : " + adress_book)
print("Username : " + username)