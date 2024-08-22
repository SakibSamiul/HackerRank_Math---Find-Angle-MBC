from math import degrees, atan2
AB = int(input())
while (AB > 100 and AB <= 0):
    AB = (input())
BC = int(input())
while (BC > 100 and BC <= 0):
    BC = (input())

degree = round(degrees(atan2(AB, BC)))
print((str(degree)), chr(176), sep="")


