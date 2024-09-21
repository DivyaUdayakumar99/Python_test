name ="Sachin"
print("His name is "+name) # two way to append the string either '+ ' or ","
print("His name is ",name)
print(type(name)) #return the trpe of the variable
print(len(name))  # return the length of the variable
num1 = int(input("Enter a integer Number ")) #input funtion take the value as string that why we convert it to using int function
num2 = float(input("enter a float number "))
num3=num1+num2
print(num3)

msg= input("enter a string ")

print('''this is Divya Udayakumar   

how are you ''') #multiline string

print(msg[0]) #print the first character
print(msg[-1]) #print the last charcter
print(msg[0:3]) #print Char from0 to 2nd index

word ="How old are you"

print(word.lower())
print(word.upper())
print(word.index('o'))
print(word[-2])

num5=7.5
from math import * #giving access to more functions inside math module
print(round(num5))
print(floor(num5))
print(ceil(num5))



