class Person:
    # define your fields
    name = "Sheep Core"
    agender = "male"
    age = 22

    # define your methods
    def getName(self):
        return self.name

    def setName(self, newname):
        self.name = newname

    def getAge(self):
        return self.age
    def getSex(self):
        return self.agender
    def showProfile(self):
        print("name: %s  agender: %s age: %s" %(self.name, self.agender, self.age))

me = Person()
me.showProfile()

you = Person()
you.name = "Marshall Lee"
you.age = 23
you.showProfile()