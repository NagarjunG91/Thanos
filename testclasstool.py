from classtools import AttrDisplay

class Person(AttrDisplay):

    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary

    def giveraise(self, percent):
        self.salary = self.salary*(1 + (percent/100))


class Manager(Person):

    def __init__(self, name, salary, xobcode ='Mgr'):
        Person.__init__(self, name, salary)
        self.xobcode = xobcode


A = Person('Raj', 30000)
B = Manager('Garuda', 40000)

print('person is', A)
B.giveraise(40)
print('Person B', B)


class Super:
    def delegate(self):
        self.action()


class Provider(Super):
    def action(self):
        print('kai zhala')


if __name__ == '__main__':
    A = Provider()
    A.delegate()

