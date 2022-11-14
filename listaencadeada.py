class no:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
    def __repr__(self):
        return '%s -> %s' % (self.dado, self.proximo)
    

class lista:
    def __init__(self):
        self.first = None
    def __repr__(self):
        return "[" + str(self.first) + "]"


    def include(self, value):
        new = no(value)
        new.next = self.first
        self.first = new
