#Depth First Search

import copy
graph = {
    'A':['B','D'],
    'B':['C','E'],
    'C':[],
    'D':['E','G','H'],
    'E':['C','F'],
    'F':[],
    'G':['H'],
    'H':[]
}
def dfs(startNode,finalNode):
    path=[]
    stack=[]

    stack.append([startNode])

    while len(stack)>0:
        path.append(stack.pop())
        node=path[-1][-1]

        for neighbor in graph[node]:
            newPath=copy.deepcopy(path[-1])

            if neighbor == finalNode:
                finalPath=copy.deepcopy(path[-1])
                finalPath.append(finalNode)
                print("Final Path", finalPath)
                return "Found goal node"

            newPath.append(neighbor)
            stack.append(newPath)

            print("Path", path)
            print("stack", stack)

dfs('A','G')

