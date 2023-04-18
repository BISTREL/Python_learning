#coding: utf-8
###LIST
COURSE = ["Phy", "Math", "Chem", "CS", "Geo", "FMath"]
COURSE1 = ["Art","Cast"]

COURSE[0] = "Geol"
COURSE.append('Miss')
COURSE.insert(2, 'Dr')
COURSE1.extend(COURSE)
COURSE1.sort()
COURSE1.reverse()

print(COURSE.index('Math'))
for index, sub in enumerate (COURSE1, start=1):
    print(index, sub)

###Tuples 
"""Doesn't support assignement (unmutable)"""

COUR = ("Phy", "Math", "Chem", "CS", "Geo", "FMath")

###SET

Ct = {"Phy", "Math", "Chem", "CS", "Geo", "FMath", "Math"}
art = {"Design", "Math", "His", "Geo", "Math"}

print(Ct.intersection(art))
print(Ct.union(art))
