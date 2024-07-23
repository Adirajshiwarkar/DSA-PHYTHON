class Node:
    def __init__(self,value):
        self.value=value
        self.next= None
    def __str__(self):
        return str(self.value)
        
class CSLinkedlist:
    # def __init__(self,value):
    #     new_node=Node(value)
    #     new_node.next=new_node
    #     self.head=new_node
    #     self.tail=new_node
    #     self.length =0
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0    
        
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:  # Stop condition for circular list
                break
            result += ' -> '
        return result
    
    def append (self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
            new_node.next=new_node
        else:
            self.tail.next=new_node
            new_node.next = self.head
            self.tail=new_node
        self.length +=1

    def prepend (self,value):
        new_node=Node(value)
        if self.length==0:
            new_node.next=new_node
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
            self.tail.next=new_node
        self.length +=1

    def insert(self,index,value):
        if index<0 or index>self.length>0:
          raise Exception("it is out of range")
        
        new_node=Node(value)

        if index==0:
         if self.length==0:
            new_node.next=self.head
            self.head=new_node
            self.tail=new_node
         else:
            new_node.next=self.head
            self.head=new_node
            self.tail.next=new_node

        elif index==self.length:
            self.tail.next=new_node
            new_node.next=self.head
            self.tail=new_node

        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
            
        self.length += 1
    

    def traversal(self):
        if not self.head:
            return
        current=self.head
        while current is not None:
            print(current.value)
            current=current.next
            if current == self.head:
                break
            
    def search(self,target):
        current=self.head
        while current is not None:
            if current.value==target:
                return True
            current=current.next
            if current==self.head:
                break

        return False

    def get(self,index):
        if index==-1:
            return self.tail
        elif index<-1 or index>self.length:
            return None
        current=self.head
        for _ in range(index-1):         
          current=current.next
        return current

    def set(self,index,value):
        temp=self.get(index)
        if temp:
            temp.value=value
            return True
        return False
    

    def popfirst(self):
        if self.length==0:
            return None
        popped_node=self.head

        if self.length==1:
            self.head=None
            self.tail=None

        else:
            self.head=self.head.next
            self.tail.next=self.head
            popped_node.next=None

        self.length -=1
        return popped_node

    def pop(self):
       if self.length==0:
            return None
       popped_node=self.tail

       if self.length==1:
            self.head=None
            self.tail=None
       else:
           temp=self.head
           while temp.next!= self.tail:
               temp=temp.next
               temp.next=self.head
               self.tail=temp

       popped_node.next=None
       self.length -=1
       return popped_node
    
    def remove(self,index):
        if index < -1 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == -1 or index == self.length-1:
            return self.pop()
        prev_node=self.get(index-1)
        popped_node=prev_node.next
        prev_node.next=popped_node.next
        popped_node.next=None
        self.length-=1
        return popped_node







    def deleteall(self):
        if self.lenth==0:
            return
        self.tail.next=None
        self.head=None
        self.tail=None
        self.length=0
        

           

cslinkedlist=CSLinkedlist()
cslinkedlist.append(10)
cslinkedlist.append(20)
cslinkedlist.append(30)
cslinkedlist.append(40)
cslinkedlist.insert(0,50)
cslinkedlist.insert(5,60)
print(cslinkedlist)
print(cslinkedlist.remove(4))
print(cslinkedlist)




        
        