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