
class Bus:
    def __init__(self, count):
        self.count = count
        self.peopleinbus = 0
        self.obj = []

    def capacity(self):
        return self.count

    def onboard(self, object):
        self.count = self.count - 1
        self.obj.append(object)

    def offboard(self, object):
        self.count = self.count + 1
        self.obj.remove(object)
