for letter in "My files":
    print(letter)
for words in "MY Dady is my hero":
    print(words)
#using for loop in lists
friends3=["Maya","Meena","Mini"]
for index in range(10):
    print(index)
for index1 in range(3,10):#print from 3 to 9
    print(index1)
print("next loop")
for index2 in range(10,2,-3):#print from 3 to 9
    print(index2)

def raise_power(basenum,pownum):
    print("your inside function")
    result=1
    for index in range(pownum):
        print(index)
        result=result * basenum
    return (result)

print(raise_power(2,5))