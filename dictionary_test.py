#Dic allows you t store a special value called Key Value
#Dic_name={"key1"="Value","Key2"="value"}
#we can't have duplicate Key values
#wecan also use Numbers as keys
month_conversions={
    "Jan":"january",
    "feb":"February",
    "mar":"March"
}

print(month_conversions)
print(month_conversions["mar"]) #Using Key we are returning orginal value
print(month_conversions.get("Jan")) #using get function
print(month_conversions.get("Jun","Not a valid Key"))

famous_songs = {"Queen": "Bohemian Rhapsody",
                "Bee Gees": "Stayin' Alive",
                "U2": "One",
                "Michael Jackson": "Billie Jean",
                "The Beatles": "Hey Jude",
                "Bob Dylan": "Like A Rolling Stone"}  # 1 and 2
print(len(famous_songs))  # 3
for key in famous_songs.keys():  # 4
    print(key)
print(famous_songs.values())  # 5
for key, value in famous_songs.items():  # 6
    print(key, value)
print(famous_songs.get("Promise of the Real", "That is not a key that appears in the dictionary."))  # 7