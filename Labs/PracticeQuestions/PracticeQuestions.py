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

# User Password

Password = "Pk36SCBL0000001123456702"

if re.search(r"\S{1}\d{2}\S{4}\d{16}" , Password):
     print("It is a verified Password")
else:
    print("Incorrect Password")






