import re

# CNIC Number

cnicNumber = "42201-3521068-1"

if re.search(r"\d{5}-\d{7}-\d{1}" , cnicNumber):
    print("It is a verified CNIC Number")
else:
    print("Incorrect Number")