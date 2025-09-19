# List=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# print(List[0])
# print(List[1])
# print(List[2])


# List=[[[1,2,3],[4,5,6]],[[10,20,30],[40,50,60]]]
# print(List[0])
# print(List[1])
# print(List[0][1])
# print(List[1][0])
# print(List[1][1])
# print(List[0][0])


# prog_Lang={101:'python',102:'java',103:'c',104:'html'}
# print(prog_Lang[101])
# print(prog_Lang[102])
# print(prog_Lang[103])
# print(prog_Lang[104])
# prog_Lang[102]='Javascript'
# print(prog_Lang)
# print(type(prog_Lang))


# cube={x:x*x*x for x in range(1,6)}
# print(cube)


class satck:
    def __init__(self):
        self.Stack=[]
    def push(self,element):
        self.Stack.append(element)
        print(f"{element} added to stack.........!")
    def isempty(self):
        return len(self.Stack)==0
    def pop(self):
        if self.isempty():
            print("stack is empty...........!")
        else:
            self.Stack.pop()
            print(f"element is removed........!")
    def peek(self):
        print(f"top element is {self.Stack[-1]}")
    def size(self):
        if self.isempty():
            print(f"stack is empty")
        else:
            print(f"length of the stack is {len(self.Stack)}")
    def dispaly(self):
        print(self.Stack)
S=Stack()
S.push(10)
S.push(20)
S.push(30)
