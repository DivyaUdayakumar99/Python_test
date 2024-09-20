#used to store a bounch of values
friends=["Maya","Meena",2,2,"Jaya"] #one list can contain multiple type(str,int.float) of items
print(friends) #print the entire list
print(friends[0]) #print the first item
print(friends[-1]) #print the last item

print(friends[1:]) #print the second and other items after that
print(friends[1:3])#print the 2nd and 3rd items

friends[1]="mohini"
print(friends[2])
print(friends)


#List Functions
lucky_num=[2,4,6,7]
print(lucky_num)
friends.extend(lucky_num) #append the lucky_num list to friends list
print(friends)
lucky_num.append(66) #append an iten to the end of the lsit
print(lucky_num)
friends.insert(2,"Jeethu") #inserting a new value the index 2, all other item after 2nd index is pushed to right
print(friends)
friends.remove("Maya") #remove an item from the list
print(friends)
lucky_num.clear() #to clear the entire list
print(lucky_num)
friends.pop()  #remove the last element
print(friends)

print(friends.index(2)) #checking whether the item is in the list. if its there it will return thr index value
print(friends.count(2))
lucky_num=[77,22,43,568]
lucky_num.sort() #asending order (only work if the list have same kind of items)
print(lucky_num)
lucky_num.reverse()
print(lucky_num)

friends2=friends.copy() #copy of the list
print(friends2)
