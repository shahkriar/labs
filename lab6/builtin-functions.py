import math
import time

#ex 1 product of all numbers in the list
def ex1():
    n = int(input("Input length: "))
    lst = []
    for i in range(n):
        lst.append(int(input()))# convert into int then add to empty list
    print(math.prod(lst)) #finding product

#ex 2 number of upper and lower case letters
def ex2():
    text = str(input("Input the text: "))
    low = sum(1 for letter in text if letter.islower())
    up = sum(1 for letter in text if letter.isupper())
    
    print('Lower case letters: ', low)
    print('Upper case letters: ', up)

#ex 3 is polindrome ?
def ex3():
    text = str(input("Input the text: "))
    if text == text[::-1]:
        print(text, "is a palindrome")
    else:
        print(text, "is not a palindrome")
    
#ex 4 find sqrt root after certain miliseconds
def ex4():
    num = int(input("Input the number: "))
    mil= int(input("Input the number of miliseconds: "))
    seconds = mil/1000 #from miliseconds to seconds
    
    time.sleep(seconds) #stop program for a time 
    result = int(math.sqrt(num))#finding sqrt root of number
    
    print('The root of ' + num + 'is ' + result + 'after ' + mil + ' miliseconds')#printing results 

#ex 5 return true if all elements in the tuple are true 
def ex5():
    tup = (True, False, True, False, True)
    false = sum(1 for i in tup if i == False)
    if false > 0:
        return False
    else:
        return True
    


ex1()
ex2()
ex3()
ex4()
ex5()
    