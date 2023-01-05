

class Queue:
    def __init__(self):
        self.Initial = None
        self.Final = None
        self.Queue = []

    def GetInitial(self):
        return self.GetInitial

    def GetFinal(self):
        return self.Final
    
    def Add(self, Element):
        self.Queue.append(Element)
        self.Final = Element
        return self.Final

    def Remove(self):
        self.Queue.pop(0)
        self.Initial = self.Queue[0]
        return self.Initial 

    def __str__(self):
        return str(self.Queue)

    def __len__(self):
        return len(self.Queue)


MyQueue = Queue()

MyQueue.Add(1)
MyQueue.Add(2)
MyQueue.Add(3)

print(MyQueue)

MyQueue.Remove()

print(MyQueue)
