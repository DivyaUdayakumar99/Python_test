#functions are bunch of codes and lines perform certain actions
def say_hi(): #function names should be in lower case, we can use _ to sepeate the word spce is not allowed
    print("Hi")

say_hi() # function without parameter

def say_hi2(name, age): #function with parameter, we can pass multiple parameter to a function
    print("hi "+name+" You are S"+age," years old")

name=input("what's your name? ")
age=input("what's your age? ")
say_hi2(name,age)

#return statement :- return information from python function

def cube(num):
    return(num*num*num)

print(cube(3))
result=cube(5)
print(result)