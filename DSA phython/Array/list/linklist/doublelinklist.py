class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None

    def __str__(self):
        return str(self.value)

class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length = 0


    def __str__(self):
        temp_node=self.head
        result=''
        while temp_node:
            result+=str(temp_node.value)
            if temp_node.next:
                result +='<->'
            temp_node=temp_node.next
        return result 
    
    def append(self,value):
        new_node=Node(value)
        if not self.head:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
        self.length +=1
       
    def prepend(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
        self.length +=1

    def traversal(self):
        current_node=self.head
        while current_node:
            print(current_node.value)
            current_node=current_node.next

    def reversetraversal(self):
        current_node=self.tail
        while current_node:
            print(current_node.value)
            current_node=current_node.prev


    def serch(self,target):
        current_node=self.head
        index=0
        while current_node:
            if current_node.value==target:
                return index
            current_node=current_node.next
            index+=1
        return -1

    def get(self,index):
        if index < self.length//2:
          current_node=self.head
          for _ in range (index):
              current_node=current_node.next
        
        else:
            current_node=self.tail
            for _ in range(self.length-1,index,-1):
                current_node=current_node.prev 
        
        return current_node
    
    def set(self,index,value):
        node=self.get(index)
        if node:
            node.value=node
            return True
        return False
        






    def insert(self,index,value):
        if index<0 or index>self.length:
            print("it is out of bound")
        if index==0:
            return self.prepend(value)
        elif index==self.length:
            return self.append(value) 
        new_node=Node(value)
        temp_node=self.get(index-1)
        new_node.next=temp_node.next
        new_node.prev=temp_node
        temp_node.next.prev=new_node
        temp_node.next=new_node
        self.length -1

    def popfirst(self):
        if not self.head:
            return None
        poppend_node=self.head
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            self.head=self.head.next
            self.head.prev=None
            poppend_node.next=None
        self.length-=1
        return poppend_node
    
    def pop(self):
        if not self.head:
            return None
        poppend_node=self.head
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            self.tail=self.tail.prev
            self.tail.next=None
            poppend_node=None
        self.length-=1
        return poppend_node

    def remove(self,index):
        if index<0 or index>= self.length:
            return None
        if index==0:
            return self.popfirst()
        if index==self.length -1:
            return self.pop()
        
        poppend_node=self.get(index)
        poppend_node.prev.next=poppend_node.next
        poppend_node.next.prev=poppend_node.prev
        poppend_node.next=None
        poppend_node.prev=None
        self.length-=1
        return poppend_node






newDDL=DoublyLinkedList()
newDDL.append(10)
newDDL.append(20)
newDDL.append(30)
newDDL.append(40)
newDDL.append(50)
newDDL.prepend(60)
print(newDDL)
# print(newDDL)
# newDDL.insert(0,100)
# print(newDDL)
# newDDL.insert(5,17)
# print(newDDL)       
newDDL.remove(2)
print(newDDL)
