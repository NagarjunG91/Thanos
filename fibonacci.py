#fibonacci


class Fibo:
    def __init__(self, count):
        self.count = count

    def getseries(self):
        fiboseries = []
        fi = 1
        for number in range(0, self.count):
            if number == 0 or number == 1:
                fi = 1
            else:
                fi = int(fi) + int(fiboseries[-2])
            fiboseries.append(fi)
        return fiboseries


i = int(input("enter the number till where you want the fibonacci series"))

a = Fibo(i)
print(a.getseries())
