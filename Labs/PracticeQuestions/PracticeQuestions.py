import re

# CNIC Number

cnicNumber = "42201-3521068-1"

if re.search(r"\d{5}-\d{7}-\d{1}" , cnicNumber):
    print("It is a verified CNIC Number")
else:
    print("Incorrect Number")


# mobileNum
    
mobileNum  = "0316-1063604"

if re.search(r"\d{4}-\d{7}" , mobileNum):
    print("It is a verified Mobile Number")
else:
    print("Incorrect Number")

# Bank Account Number

banKAccountNumber = "Pk36SCBL0000001123456702"

if re.search(r"\S{2}\d{2}\S{4}\d{16}" , banKAccountNumber):
     print("It is a verified  banK Account Number")
else:
    print("Incorrect Account Number")

# data format 

date = "2016-06-10"

if re.search(r"\b(19\d\d|20\d\d)-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])\b" , date):
     print("It is a verified  date format")
else:
    print("Incorrect date format")

# User Email
    
email = "sameersattar@gmail.com kashif@gmail.com ali@gmail.com"

print(re.findall(r"[\w._%]{0,20}@[\w-].[A-Za-z]{2,3}", email))
print(len(re.findall(r"[\w._%]{0,20}@[\w-].[A-Za-z]{2,3}", email)))






