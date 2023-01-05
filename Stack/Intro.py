
class Stack:
    def __init__(self):
        self.Top = None
        self.Stack = []

    def GetTop(self):
        return self.Top
    
    def Add(self, Element):
        self.Top = Element
        self.Stack.append(Element)
