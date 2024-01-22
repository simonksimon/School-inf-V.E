#https://dudo.gvpt.sk/programujeme/zasobnik/stack.html
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


op_stack=[]
emptylist=[]
outputlist=[]
inp=input("Input: ")
čísla="0123456789"
znaky="*/+−"
emptylist=inp.split()
ops=False
precedence={"+":"*/+−","-":"*/+−","*":"*/","/":"*/"}
for i in range(len(emptylist)):
    if emptylist[i] in čísla:
        if ops==False:
            outputlist.append(emptylist[i])
        else: op_stack.append(emptylist[i])

    if emptylist[i]=='(':
        op_stack.append(emptylist[i])
        lp=i
        ops=True
    if emptylist[i]==')':
        for y in range(len(op_stack)):
            if op_stack[0] in znaky:
                outputlist.append(op_stack[0])
            del op_stack[0]
    if emptylist[i] in znaky:
        o=0
        for y in range(len(op_stack)):
            u=y-o
            #if op_stack[y] in znaky:
                #if op_stack[y]=="+":
                #if op_stack[y] == "-":
                #if op_stack[y] == "*":
                #if op_stack[y] == "/":
            if op_stack[u] in precedence[emptylist[i]]:
                outputlist.append(op_stack[u])
                del op_stack[u]
                o+=1
        op_stack.append(emptylist[i])
o=0
for i in range(len(op_stack)):
    u=i-o
    if op_stack[u] in znaky:
        outputlist.append(op_stack[u])
        del op_stack[u]
        o+=1

operand_stack=[]
for i in range(len(outputlist)):
    if outputlist[i] in čísla:
        operand_stack.append(int(outputlist[i]))
    if outputlist[i] in znaky:
        temp=[]
        s=0
        while len(temp)<1 and s<100:
            s+=1
            u=s-o
            if operand_stack[-u] in čísla:
                temp.append(operand_stack[-u])
                del operand_stack[-u]
                o+=1
        if outputlist[y] == "+": operand_stack.append(temp[0]+temp[1])
        if outputlist[y] == "-": operand_stack.append(temp[0]-temp[1])
        if outputlist[y] == "*": operand_stack.append(temp[0]*temp[1])
        if outputlist[y] == "/": operand_stack.append(temp[0]/temp[1])
print(operand_stack)