import re

name = "sameer sattar@#"

match1 = re.findall("[atr]" , name)
print(match1) # ['a', 'r', 'a', 't', 't', 'a', 'r']

match2 = re.findall("[^atr]" , name)
print(match2) # ['s', 'm', 'e', 'e', ' ', 's']

match3 = re.findall("[a-z]" , name)
print(match3) # ['s', 'a', 'm', 'e', 'e', 'r', 's', 'a', 't', 't', 'a', 'r']

match5 = re.findall("[@]" , name)
print(match5) # ['@']

decimalName = "sameerrdd0022299"

match4 = re.findall("[0-2]" , decimalName)
print(match4) # ['0', '0', '2', '2', '2']

match5 = re.findall("[9]" , decimalName)
print(match5) # ['9', '9']



