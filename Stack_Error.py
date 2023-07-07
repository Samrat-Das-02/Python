#Write a program that implements a stack data structure of specific size. If the stack is full and we are trying to push an item, then an IndexError exception should be raised. Similarly, if the stack is empty, then an IndexError exception should be raised.
class Stack:
    def __init__(self,size):
        self.size=size
        self.stack=[]
    def push(self,item):
        if(len(self.stack)==self.size):
            raise IndexError("The stack is full ,can't push")
        self.stack.append(item)
    def pop(self):
        if (len(self.stack)==0):
            raise IndexError("The stack is empty ,can't pop")
        return self.stack.pop()
    
    
size=int(input("Enter the size of the stack : "))
stack=Stack(size)
for i in range(size):
    item=int(input("Enter the item : ")) 
    stack.push(item)
try:    
    stack.push(4)
except IndexError as e:
    print("Error :",e)
for i in range(size):
    print("The item ",stack.pop()," is popped fromm the stack ")
try :
    stack.pop()
except IndexError as e :
    print("Error : ",e)