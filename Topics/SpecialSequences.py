# Special Sequences in Regukar Expression
import re

a = "sameer sattar"

match = re.search(r'\Asa' , a)
print(match) # <re.Match object; span=(0, 2), match='sa'>

match1 = re.search(r'ar\b' , a)
print(match1) # <re.Match object; span=(11, 13), match='ar'>

match2 = re.search(r'\bsa' , a)
print(match2) # <re.Match object; span=(0, 2), match='sa'>

match3 = re.search(r'sa\B' , a)
print(match3) # <re.Match object; span=(0, 2), match='sa'>

match4 = re.search(r'\Bar' , a)
print(match4) # <re.Match object; span=(11, 13), match='ar'>

b = "222sameer sattar222 "

match5 = re.findall(r'\d' , b)
print(match5) # ['2', '2', '2', '2', '2', '2']

match6 = re.findall(r'\D' , a)
print(match6) # ['s', 'a', 'm', 'e', 'e', 'r', ' ', 's', 'a', 't', 't', 'a', 'r']

match7 = re.findall(r'\s' , b)
print(match7) # [' ', ' ']

match8 = re.findall(r'\S' , a)
print(match8) # ['s', 'a', 'm', 'e', 'e', 'r', 's', 'a', 't', 't', 'a', 'r']

match9 = re.findall(r'\w' , b)
print(match9) # ['2', '2', '2', 's', 'a', 'm', 'e', 'e', 'r', 's', 'a', 't', 't', 'a', 'r', '2', '2', '2']

match10 = re.findall(r'\W' , a)
print(match10) # [' ']

match11 = re.search(r'ar\Z' , a)
print(match11) # <re.Match object; span=(11, 13), match='ar'>






