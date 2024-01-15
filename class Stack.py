class Stack:
    def __init__(self):
        self.values=[]

    def isEmpty(self):
        if len(self.values)==0:
            return True
        else:
            return False
    def push(self,value):
        self.values.append(value)
    def pop(self):
        if not(self.isEmpty()):
            return self.values[-1]
        else:
            raise IndexError("Stack is Empty.")

zas1=Stack()
print(zas1.isEmpty)
#b=zas1.pop()
b=zas1.push(5)
print(zas1.pop())