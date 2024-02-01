import re

def checkStartAndEndString(str):
    if re.search("^apple.*abc$", str):
        print("Match Found")
    else:
        print("Match Not Found")
    
checkStartAndEndString("apple abc") # Match Found
