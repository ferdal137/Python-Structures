#Linked List

#Create the node class

class Node:
    def _init_(sekf,Value):
        self.Value = Value
        self.next = None
    
    def _str_(self):
        return str(self.Value)

class LinkedList:
    def _init_(self)
        self.First = None
        self.Size = 0 

    def Append(self, Value):
        MyNode = Node(Value)
        if self.Size == 0:
            self.First = MyNode
        else:
            Current = self.First
            
