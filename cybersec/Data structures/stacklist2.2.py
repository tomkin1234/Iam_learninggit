from pickle import TRUE
from secrets import choice


stack =[]

def push():
    element = input('pleas, input an element: ')
    stack.append(element)
    print(stack)

def pop():    
    #checking if stack is empty
    if not stack:
        print('stack is empty')   
    else:
        e = stack.pop()
        print('removed element: ',e)
        print(stack)

while True:
    print('Hi, we will create a stack! Please, select the operation: 1=push, 2=pop, 3=quit.')
    choice = int(input())
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        break
    else:
        print('please, enter correct operation.')
