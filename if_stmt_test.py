is_female=True
if is_female: #if is_male varibale value is true this if stmt will print the o/p else the else stmt
    print("you are a female")
else:
    print("you are a male")

# we can use or , and key words in if stmt

is_male=True
is_tall=False

if is_male or is_tall:
    print("you are male or tall or both")
else:
    print("you are neither male nor tall")

if is_male and is_tall:
    print("you are a tall male")
elif is_male and not(is_tall):
    print("you are a short male")
elif not(is_male) and (is_tall):
    print("you are not a male but you are tall")
else:
    print("you are either not male or not tall or both")

    

 