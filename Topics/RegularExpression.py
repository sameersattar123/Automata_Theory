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

match