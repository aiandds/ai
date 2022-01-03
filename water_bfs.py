from collections import deque
def water_jug_bfs(j1, j2, water):
    visited = set()
    q = deque()
    q.append((0, 0))
    print("\n", (0, 0))
    visited.add((0, 0))
    isSolvable = False
    target = [(0, water), (water, 0)]
    while(len(q) != 0):
        size = len(q)
        print("\n\n***\n")
        for _ in range(size):
            curr = q.popleft();
            if(curr in target):
                isSolvable = True
                break
            curr_j1, curr_j2 = curr[0], curr[1]
            possiblities = []
            possiblities.append((j1, curr_j2))
            possiblities.append((curr_j1, j2))
            possiblities.append((0, curr_j2))
            possiblities.append((curr_j1, 0))
            if(curr_j1 != 0 and curr_j2 != j2):
                total_water = curr_j1 + curr_j2
                if(total_water <= j2): possiblities.append((0, total_water))
                else: possiblities.append((total_water-j2, j2))
            if(curr_j1 != j1 and curr_j2 != 0):
                total_water = curr_j1 + curr_j2
                if(total_water <= j1): possiblities.append((total_water, 0))
                else: possiblities.append((j1, total_water-j1))
            for poss in possiblities:
                if(poss not in visited):
                    x, y = poss[0], poss[1]
                    q.append((x, y))
                    print((x, y), end=" ")
                    visited.add((x, y))
        if(isSolvable == False):
            print("Not possible to work with these inputs")
if __name__=="__main__":
    jug1 = int(input("Enter jug 1 capacity : "))
    jug2 = int(input("Enter jug 2 capacity : "))
    water = int(input("Enter final capacity of water needed : "))
    water_jug_bfs(jug1, jug2, water)
