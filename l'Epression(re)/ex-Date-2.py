import re
 

s =  ["20",
    "/",
    "03",
    "/",
    "2022"
]
s.reverse()
print(s)



s= "19/03/2022"
l = re.split("," ,s)
s1= ("{l[2]} - {l[1]} - {l[0]}")
 
print(s1)














