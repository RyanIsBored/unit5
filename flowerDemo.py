#Ryan Jones
#4/26/18
#flowerDemo.py - vowelWordDemo.py I misheard the name - treat strings as lists

words = input('Enter some words: ').split(' ')

for w in words:
    if w[0] in 'AEIOUaeiou': #starts with a vowel
        print(w)
