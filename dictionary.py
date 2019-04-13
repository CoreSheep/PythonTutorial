#1. create a dictionary
students = {}
students[20164586] = "Sheep Core"
students[20164433] = "Marshall Lee"
students[20165544] = "Paul Brown"

print(students)

#2. iterations for dictionary
for id, name in students.items():
    print("id: %d, name: %s" %(id, name))

students.pop(20165544)
if 20164586 in students:
    print("There is an id called 20164586")
    