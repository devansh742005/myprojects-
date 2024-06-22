graph = [0:[1,2], 1:[2], 2[0,3] , 3:[3]]
start = 0

stack = [start]
visted = set()
while stack:
    verterx = stack.pop()
    if verterx not in visted:
        print(vert)