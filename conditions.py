#1. ==, !=, and, or
name = "sheep core"
age = 22
food = "apple"
if name == "sheep core" and age >= 18:
    print("You are very handsome.")
elif food == "apple" or food == "banana":
    print("You're not my type, but we both love apple or banana")

#2. in operator
names = []
names.append("sheep core".capitalize())
names.append("Marshall Lee")

myname = "Paul Brown"
youname = "sheep core"
if youname.capitalize() in names:
    print('"%s" is on the list %s.' %(youname, names))
if myname not in names:
    print('"%s" is not on the list %s.' %(myname, names))

#3. is operator similar with instanceof in Java
nums = [1, 2, 3]
x = nums  #x is reference of nums you can also call that is a copy of nums
if x is nums:
    print("x is an instance of %s" %nums)



