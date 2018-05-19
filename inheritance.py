class ClassMember:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        print('Initiated school member {}'.format(self.name))

    def tell(self):
        print('Name: {} Age: {} Address: {}'.format(self.name, self.age, self.address), end=" ")


class ClassTeacher(ClassMember):
    def __init__(self, name, age, address, salary):
        ClassMember.__init__(self, name, age, address)
        self.salary = salary
        print('Initiated class teacher {}'.format(self.name))

    def tell(self):
        ClassMember.tell(self)
        print('Salary: {:d}'.format(self.salary))


class ClassStudent(ClassMember):
    def __init__(self, name, age, address, marks):
        ClassMember.__init__(self, name, age, address)
        self.marks = marks
        print('Initialized class student {}'.format(self.name))

    def tell(self):
        ClassMember.tell(self)
        print('Marks: {:d}'.format(self.marks))


t = ClassTeacher('Raja', 40, 'Vpura', 50000)
s = ClassStudent('Ram', 14, 'Vpura', 75)

members = [t,s]
for member in members:
    member.tell()





