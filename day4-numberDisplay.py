#Maurel ZODOGANHOU
#DAY4-DJANGO-CHALLENGE
"""
This Program will ask the user to enter a 10-character telephone number in the format of XXX-XXX-XXXX. 
The application should display the telephone number with any alphabetic characters that
appeared in the original translated to their numberic equivalent. For example,
if the user enters 555-GET-FOOD the application should display 555-438-3663
"""
 
phoneNum = input("Enter the number in the format of XXX-XXX-XXXX: ")
 
phoneNum= phoneNum.split('-')
 
for var in phoneNum[1:2]:
      for char in phoneNum:
            if char == 'A' or char == 'B' or char == 'C':
                  char == '2'
            elif char == 'D' or char == 'E' or char == 'F':
                  char = '3'
            elif char == 'G' or char == 'H' or char == 'I':
                  char = '4'
            elif char == 'J' or char == 'K' or char == 'L':
                  char = '5'
            elif char == 'M' or char == 'N' or char == 'O':
                  char = '6'
            elif char == 'P' or char == 'Q' or char == 'R' or char == 'S':
                  char = '7'
            elif char == 'T' or char == 'U' or char == 'V':
                  char = '8'
            elif char == 'W' or char == 'X' or char == 'Y' or char == 'Z':
                  char = '9'
 
print(phoneNum)