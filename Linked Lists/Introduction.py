#Linked List

#Create the node class

class Node:
    def _init_(sekf,Value):
        self.Value = Value
        self.Next = None
    
    def _str_(self):
        return str(self.Value)

#Create the Linked List

class LinkedList:
    def _init_(self)
        self.First = None
        self.Size = 0 
 
    def Append(self, Value):      #Method to append a node in the final of the list
        MyNode = Node(Value)
        if self.Size == 0:
            self.First = MyNode
        else:
            Current = self.First
            while(Current.Next!=None):
                Current = Current.Next
            Current.Next = MyNode
        
        self.Size += 1

        return MyNode

