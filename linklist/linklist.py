class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
    

        
class LinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.lenght=1



new_linkedlist=LinkedList(10)
print(new_linkedlist.head.value)
        
        
             