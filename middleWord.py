#Ryan Jones
#4/23/18

e=input('Enter a list of words: ').split(' ')
lengthlist = int(len(e))
if lengthlist%2==0:
    print(e[lengthlist/2-1],e[lengthlist/2])