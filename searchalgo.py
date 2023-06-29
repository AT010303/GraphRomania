from graph import *
from node import node
from pqueue import priorityQueue

Goal = 'Bucharest'
Initial = 'Arad'
start = node(Initial,None,0)


def notVisited(i,Visited):
    for j in Visited:
        if i == j:
            return False
    return True



def DFS():
    
    Visited = []
    Stack = []
    nodeGenrated=0
    Stack.insert(0,start)
    while Stack:
        curr = Stack.pop(0)
        Visited.append(curr.name)
        if curr.name == Goal:
            print("DFS (rightmost node selected first)")
            print(curr.path)
            print("Depth : ",curr.Depth)
            print("Path Cost : ",curr.gn)
            print("Number of nodes generated are : " , nodeGenrated)
            print("---"*50)
            return curr
        generated = curr.explore()
        for i in generated:
            if notVisited(i,Visited):
                nodeGenrated += 1
                d = curr.Depth + 1
                state = node(i,curr,d)
                Stack.insert(0,state)

def DepthLtdS():

    Depth = 2
    nodeGenrated = 0

    while True:
        Visited = []
        Stack = []
        Stack.insert(0,start)
        curr = start
        while Stack:
            curr = Stack.pop(0)
            Visited.append(curr.name)
            if curr.name == Goal:
                print("Depth Limited Search (Depth = 3)")
                print(curr.path)
                print("Depth : ",curr.Depth)
                print("Path Cost : ",curr.gn)
                print("number of node genrated : " , nodeGenrated)
                print("---"*50)
                return curr
            generated = curr.explore()
            for i in generated:
                if Depth < curr.Depth:
                    pass
                elif notVisited(i,Visited):
                    d = curr.Depth + 1
                    state = node(i,curr,d)
                    Stack.insert(0,state)
                    nodeGenrated+=1




def IDDFS():

    Depth = 0
    nodeGenrated=0
    
    while True:
        print("iteration" , Depth+1)
        Visited = []
        Stack = []
        Stack.insert(0,start)
        curr = start
        while Stack:
            curr = Stack.pop(0)
            Visited.append(curr.name)
            if curr.name == Goal:
                print("Iterative deepening Depth First Search")
                print(curr.path)
                print("Depth : ",Depth+1)
                print("Path Cost : ",curr.gn)
                print("number of node generated : " , nodeGenrated)
                print("---"*50)
                return curr
            generated = curr.explore()
            for i in generated:
                if Depth < curr.Depth:
                    pass
                elif notVisited(i,Visited):
                    d = curr.Depth + 1
                    state = node(i,curr,d)
                    Stack.insert(0,state)
                    nodeGenrated+= 1
        Depth += 1

def BestFirstSearch():
    Queue = priorityQueue()
    Queue.push(start, start.hn)
    nodeGenrated = 0

    while True:
        tup = Queue.pop()
        curr = tup[1]
        if curr.name == Goal:
            print('Best first search')
            print(curr.path)
            print("Depth : ",curr.Depth)
            print("Path Cost : ",curr.gn)
            print("number of node generated : " , nodeGenrated)
            print("---"*50)
            return curr
        E = curr.explore()
        
        for name in E:
            d = curr.Depth + 1
            new_node = node(name, curr, d)
            Queue.push(new_node, new_node.hn)
            nodeGenrated+=1


def Astar():
    Queue = priorityQueue()
    Queue.push(start,start.fn)
    nodesGenrated = 0

    while True:
        tup = Queue.pop()
        curr = tup[1]
        if curr.name == Goal:
            print('Astar')
            print(curr.path)
            print("Depth : ",curr.Depth)
            print("Path Cost : ",curr.gn)
            print(f"number of nodes generated :  {nodesGenrated}")
            print("---"*50)
            return curr
        E =[]
        E = curr.explore()

        for name in E:
            d = curr.Depth + 1
            new_node = node(name,curr,d)
            nodesGenrated +=1
            Queue.push(new_node,new_node.fn)
