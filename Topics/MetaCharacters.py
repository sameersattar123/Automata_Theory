# MetaCharacters in Regukar Expression

import re

email = "sameer.sattar@gmail.com"

match =  re.search(r"\." , email)
print(match) # <re.Match object; span=(6, 7), match='.'>

match2 =  re.findall(r"[a]" , email)
print(match2)         # ['a', 'a', 'a', 'a']

match3 = re.search(r"^s" , email)
print(match3) # <re.Match object; span=(0, 1), match='s'>

match4 = re.search(r"^a" , email)
print(match4) # None

match5 = re.search(r".com$" , email)
print(match5) # <re.Match object; span=(19, 23), match='.com'>

match6 = re.search(r"sameer$" , email)
print(match6) # None

match7 = re.findall(r"sa" , email)
print(match7) # ['sa' , 'sa']

match8 = re.findall(r"f" , email)
print(match8) # []

match8 = re.search(r"sam|sat" , email)
print(match8) # <re.Match object; span=(0, 3), match='sam'>

match8 = re.findall(r"sa?m" , email)
print(match8) # ['sam']

match9 = re.findall(r"sa*m" , email)
print(match9) # ['sam']

match9 = re.findall(r"sam+e" , email)
print(match9) # ['same']

match10 = re.findall(r"sa{1}" , email)
print(match10) # ['sa' , 'sa']

match11 = re.findall(r"(s)a" , email)
print(match11) # ['s' , 's']






