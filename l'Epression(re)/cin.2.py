import re

a = "JF96522"
b = re.search(r"[^0-8]" , a)
print(b)
if b:
    print("yes")
else :
    print("No")



