#1. for and while(in, else, continue, break, range method)
nums1 = range(5) #from: 0 to: 5 skip: 1
nums2 = range(2, 5) #from: 1 to: 5 skip: 1
nums3 = range(0, 5, 2)

print(nums1)
print(nums2)
count = 0
while count <= 3:
    if count == 2:
        continue
    print(count)
    count += 1
else:
    print("count stops at %d" %count)

count = 0
for x in nums2:
    if(x % 2 == 0):
        count += 2;
        break
    count += 1
else:
    print("These codes will not be executed")


