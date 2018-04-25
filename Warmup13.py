#Ryan Jones
#4/25/18

from random import randint

h =[]
i=1
while i<=20:
    h.append(randint(1,100))
    i=i+1
print(sum(h))
print(min(h))
print(max(h))