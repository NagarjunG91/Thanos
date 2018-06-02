class Person:
    def __init__(self, name, salary=0, job=None):
        self.name = name
        self.salary = salary
        self.job = job

    def __repr__(self):
        return '(%s, %s, %s)' % (self.name, self.salary, self.job)

    def giveraise(self, percent):
        self.salary = int(self.salary * (1 + percent))

    def lastname(self):
        return self.name.split()[-1]


class Development:
    def __init__(self, *args):
        self.members = list(args)

    def __repr__(self):
        return '%s' % self.members

    def addMember(self, person):
        self.members.append(person)

    def giveRaise(self, percent):
        for person in self.members:
            person.giveraise(percent)

    def show(self):
        for person in self.members:
            print(person)


class Tester:
    def __init__(self, *args):
        self.mem = list(args)

    def __repr__(self):
        return '%s' % self.mem

if __name__ == '__main__':
    bob = Person('bob smith')
    bob.salary = 10000
    sue = Person('Sue Jones',salary=10000)
    sue.giveraise(.1)
    k = bob.lastname()
    sue.job = 'dev'
    mary = Person('mary kom', salary=10000, job= 'test')
    sam = Person('Sam Winchester', salary=20000, job= 'testLead')
    dev=Development(bob, sue)
    dev.giveRaise(.1)
    print(dev)
    dev.addMember('dog')
    print(dev)

    test= Tester(mary, sam)
    print(test)
