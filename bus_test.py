from bus import Bus
from person import Person

if __name__ == '__main__':

    A = Bus(10)

    print('bus capacity is ',A.capacity())

    Sam = Person('Sam', 25000)
    A.onboard(Sam)
    Jeo = Person('Jeo', 50000)
    A.onboard(Jeo)
    print('check object {}'.format(A.obj))
    print('Capacity {}'.format(A.capacity()))
    A.offboard(Sam)
    print('Samoff object {}'.format(A.obj))
    print('Capacity new {}'.format(A.capacity()))
