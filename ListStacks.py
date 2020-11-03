# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 15:50:49 2020

@author: VIRUS
"""

"""
stack = []

def Push():
    element = input("Enter a number: ")
    stack.append(element)
    print("Element added: ",stack)

def PopElement():
    if not stack:
        print("stack underflow!")
    else:
        elem = stack.pop()
        print("Removed Element: ", elem)
        print(stack)

def PrintStack():
    if not stack:
        print("Stack Underflow")
    else:
        for i in stack:
            print(i)
        
while True:
    print("Select the operation to be performed: 1.Push, 2.Pop, 3.Print Stack, 4.print top most elem 5.Quit")
    choice = int(input())
    if choice == 1:
        Push()
    elif choice == 2:
        PopElement()
    elif choice == 3:
        PrintStack()
    elif choice == 4:
        print("The top most element is: ",stack[-1])
    elif choice == 5:
        break
    else:
        print(stack)
        
"""

#example 2
#impleamenting stack using list
stack = []

#a function pushing elements into a stack
def Push():
    element = int(input("Enter an element: "))
    stack.append(element)
    print("Element added in the stack is: ",element)

#a function poping elements from a stack
def Pop():
    if not stack:
        print("Stack underflow")
    else:
        value = stack.pop()
        print("Element poped: ", value)
        
#a function displaying the top most element in a stack
def PrintTop():
    if not stack:
        print("Stack underlow")
    else:
        print("The top most element in the stack is: ",stack[-1])
        

while True:
    print("Choose an option: 1.Push, 2.pop, 3.Print top elem, 4.Print stack, 5.Quit")
    choice = int(input())
    if choice == 1:
        Push()
    elif choice == 2:
        Pop()
    elif choice == 3:
        PrintTop()
    elif choice == 4:
        print(stack)
    elif choice == 5:
        break
    else:
        print("Enter a valid choice!")