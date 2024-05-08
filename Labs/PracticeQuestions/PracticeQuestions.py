import re

# # CNIC Number 

# def checkCnicNumber(number): 
#      if re.search(r"\d{5}-\d{7}-\d{1}" , number):
#           print("It is a verified CNIC Number")
#      else:
#           print("Incorrect Number")

# num = input("Enter any CNIC Number: ") 

# checkCnicNumber(num) 


# # mobileNum
# def checkMobileNumber(mobileNum):

#       if re.search(r"\d{4}-\d{7}" , mobileNum):
#           print("It is a verified Mobile Number")
#       else:
#         print("Incorrect Number")

# mobileNum = input("Enter any Mobile Number: ")

# checkMobileNumber(mobileNum)

# # Bank Account Number
# def checkBankAccountNumber(accountNum):

#        if re.search(r"\S{2}\d{2}\S{4}\d{16}" , accountNum):
#            print("It is a verified  banK Account Number")
#        else:
#            print("Incorrect Account Number")

# accountNumber = input("Enter any String: ")

# checkBankAccountNumber(accountNumber)


# # data format 
# def checkDateFormate(date):

#     if re.search(r"\b(19\d\d|20\d\d)-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])\b" , date):
#         print("It is a verified  date format")
#     else:
#         print("Incorrect date format")

# date = input("Enter any date: ")

# checkDateFormate(date)

# # Floating point
# def checkFloatingPoint(num):
#     if re.search("^\d+(\.\d+)?$",num):
#         print("Match found: It's a floating point number")
#     else:
#         print("Match not found: It's not a floating point number")

# num = input("Enter any String: ")

# checkFloatingPoint(num)

# Debit /Credit Card
def check_card_type(card_number):
    visa_pattern = r'^4[0-9]{12}(?:[0-9]{3})?$'
    mastercard_pattern = r'^5[1-5][0-9]{14}$'
    
    if re.match(visa_pattern, card_number):
        print("Valid card number.")
        print("This is a Visa card.")
    elif re.match(mastercard_pattern, card_number):
        print("Valid card number.")
        print("This is a Mastercard.")
    else:
        print("Invalid card number.")
num = input("Enter any card number: ")

check_card_type(num)

# # User Email
# email = "sameersattar@gmail.com kashif@gmail.com ali@gmail.com"

# print(re.findall(r"[\w._%]{0,20}@[\w-].[A-Za-z]{2,3}", email))
# print(len(re.findall(r"[\w._%]{0,20}@[\w-].[A-Za-z]{2,3}", email)))








