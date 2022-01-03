from collections import deque
def makeTuple(grid):
    return tuple(tuple(ele) for ele in grid)
def makeList(grid):
    return [[grid[i][j] for j in range (3)] for i in range (3)]

def printPath(target, parent):
    res = []
    curr = target
    src = -1
    while(curr != src):
        res.append(curr)
        curr = parent[curr]
    print("\nResult : \n")
    while(len(res) != 0):
        curr = res.pop()
        for i in range(3):
                for j in range(3):
                    print(curr[i][j], end=" ")
                print()
        print(" \n*********\n ")
def puzzle_bfs(start, end, zero):
    q = deque()
    vis = set()
    parent = dict()
    parent[makeTuple(start)] = -1
    q.append((makeTuple(start),zero))
    vis.add(makeTuple(start))
    end=makeTuple(end)
    isSolvable = False
    while(len(q) !=0):
        curr_item = q.popleft()
        curr_state = curr_item[0]
        zero = curr_item[1]
        x, y = zero[0], zero[1]
        possiblities = []
        if(curr_state == end):
            isSolvable = True
            break
        if(x!=0): possiblities.append((x-1,y))
        if(x!=2): possiblities.append((x+1,y))
        if(y!=0): possiblities.append((x, y-1))
        if(y!=2): possiblities.append((x, y+1))
        for poss in possiblities:
            new_x, new_y = poss[0], poss[1]
            temp_state = makeList(curr_state)
            temp_state[x][y], temp_state[new_x][new_y] = temp_state[new_x][new_y], 0
            temp_state = makeTuple(temp_state)
            if(temp_state not in vis):
                q.append((temp_state, poss))
                vis.add(temp_state)
                parent[temp_state] = curr_state
  
    if(isSolvable):
        printPath(end, parent)

    else:
         print("Cant work with these inputs")

if __name__ == "__main__":
   start, end = [], []
   start= []
   print("Enter the initial configuration")
   for i in range(3):
       l=list(map(int,input().split()))
       start.append(l)
   end = []
   print("Enter the final configuration")
   for i in range(3):
       l=list(map(int,input().split()))
       end.append(l)
   zero = tuple()
   for i in range(3):
       for j in range(3):
           if(start[i][j] == 0):
               zero = (i, j)
               break
   puzzle_bfs(start, end, zero)
