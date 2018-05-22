class Bankaccount:
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        self.balance -= amount
        print('new balance after withdraw {}'.format(self.balance))
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        print('new balance after deposit {}'.format(self.balance))
        return self.balance


class MinBalAcc(Bankaccount):
    def __init__(self, minimum_bal):
        Bankaccount.__init__(self)
        self.minimum_bal = minimum_bal

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_bal:
            print('please maintain minimum balance of ', self.minimum_bal)
        else:
            Bankaccount.withdraw(self, amount)


while True:

    a = int(input('please enter minimum balance you want to keep:'))
    newaccount = MinBalAcc(a)

    newaccount.deposit(a)
    print('minimum balance deducted')

    b = int(input('Please deposit an amount:'))
    newaccount.deposit(b)

    c = int(input('Please withdraw an amount:'))
    newaccount.withdraw(c)
    d = input('Do you want to Exit (Y/N) :')
    if d == 'Y':
        break
    else:
        continue


def atm(self, amount):
    if self.balance - amount < self.minimum_bal:
        print('no balance')
    else:
        self.balance -= amount
        print('new balance after ATM withdraw is {}'.format(self.balance))
    return self.balance


newaccount.memo = atm

e = input('Do you want ATM withdraw (Y/N) :')
if e == 'Y':
    g = int(input('Please enter withdrawal amt: '))
    newaccount.memo(newaccount, g)




