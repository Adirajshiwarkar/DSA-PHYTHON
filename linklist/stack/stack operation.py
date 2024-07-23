class stack:
    def __init__(self):
        self.list=[]
        
    

    def __str__(self):
        values=self.list.reverse()
        values=[str (x) for x in self.list]
        return '\n'.join(values)
    

    def isEmpty(self):
        if self.list==[]:
            return True
        else:
            return False
        
    def push(self,value):
        self.list.append(value)
        

customstack=stack() 
customstack.push(1)
customstack.push(2)
customstack.push(3)
print(customstack) 





