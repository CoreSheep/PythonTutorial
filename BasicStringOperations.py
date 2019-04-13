#1. method len
print("I hava an 'apple', " + '"you have a "pen"')
print("Length of 'apple' is %d" %len("apple"))

#2. method index
print("index of e in 'sheepcore' is %d" %"sheepcore".index('e'))

#3. capitalize the first letter of string
print("sheepcore".capitalize())

#4. count
print("sheepcore".count('e'))

#5. upper and lower
print("sheepcore".upper())
print("SHEEPCORE".lower())

#6. startswith and endswith
name = "Sheep Core"
print(name.startswith("Sheep"))
print(name.endswith("core".capitalize()))

#7. split words with delimiter
phrase = "I love python, Java and Koltlin"
print(phrase.split(" ", 2))  #delimiter and maxsize to modify

#8. slice of string [from:to:skip]
print('substring of "sheep core" from 0 to 5 %s' %name[0:5])
print('substring of "sheep core" from 0 to 5 %s' %name[:5:1])

#8.2 slice of string reverse a string using skip '-' represents opposite direction
print('reverse "%s": %s' %(name, name[::-1]))

#8.3 using skip to display odds and evens
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("odds of nums: %s" %nums[::2])
print("evens of nums: %s" %nums[1::2])



