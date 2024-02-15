import re 

result = 'John has scored 90 marks Sameer has scored 40 marks Kashif has scored 60 marks'

marks  = re.findall(r'\d+' , result)
print(marks)

names  = re.findall(r'[A-Z][a-z]*' , result)
print(names)

p = re.compile(r"\d+")
print(re.findall(p , result))

m = re.compile(r"[A-Z][a-z]*")
print(re.findall(m , result))

m = re.compile(r"[A-Z][a-z]*")
print(re.findall(m , result))

print(re.split(r"[A-Z][a-z]*", result))

print(re.sub("\s+" , "", result))
print(re.subn("\s+" , "", result))
print(re.subn("\d+", "20", result))

print(re.escape(result))

print(re.search("\d+", result))





