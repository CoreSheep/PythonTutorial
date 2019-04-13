# functions in python

def max(input):
    maxnum = 0
    for x in input:
        if x > maxnum:
            maxnum = x
    return maxnum

input = range(0, 10, 2)
print(input)
print(max(input))
