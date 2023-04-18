#coding: utf-8

COURSE = ["Phy", "Math", "Chem", "CS", "Geo", "FMath"]
COURSE1 = ["Art","Cast"]

COURSE.append('Miss')
COURSE.insert(2, 'Dr')
COURSE1.extend(COURSE)
COURSE1.sort()
COURSE1.reverse()

print(COURSE.index('Math'))
for index, sub in enumerate (COURSE1, start=1):
    print(index, sub)

