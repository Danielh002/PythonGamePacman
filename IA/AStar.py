def getInitialScores(map):
    res=[]
    for i in map:
        l=[]
        for j in i:
            l.append(100000)
        res.append(l)
    return res
def h(inicial,final):
    #return abs((inicial[0]-final[0]))+abs((inicial[1]-final[1]))
    return ((inicial[0]-final[0])**2+(inicial[1]-final[1])**2)**(1/2.0)
def getMinF(openSet,fScore):
    current=res=openSet[0]
    comparacion=fScore[res[0]][res[1]]
    i=1
    while(i<len(openSet)):
        current=openSet[i]
        if(fScore[current[0]][current[1]]<comparacion):
            res=current
            comparacion=fScore[current[0]][current[1]]
        i+=1
    return res #tenia current erro garrafal
def AStar(map,inicial,final,heuristic):
    #rosado 3 adelante de la direccion de pacman
    #inspirado en https://en.wikipedia.org/wiki/A*_search_algorithm
    #print(inicial,final)
    openSet=[inicial]
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    closedSet=[]
    gScore=getInitialScores(map)
    gScore[inicial[0]][inicial[1]]=0
    fScore=getInitialScores(map)
    fScore[inicial[0]][inicial[1]]=heuristic(inicial,final)
    cameFrom={}
    while(len(openSet)!=0):
        current=getMinF(openSet,fScore)
        openSet.remove(current)
        closedSet.append(current)
        if(current==final):
            for j in fScore:
                #print(j)
                pass
            return reconstruct_path(cameFrom,current) #TODO hay que cambiar

        i=0
        while(i<len(dx)):
            neighbor=(current[0]+dy[i],current[1]+dx[i])
            if(neighbor[0]<len(map) and neighbor[0]>=0 and neighbor[1]<len(map[0]) and neighbor[1]>=0 and (map[neighbor[0]][neighbor[1]]!=1)):
                if(not neighbor in closedSet):
                    if(not neighbor in openSet):
                        openSet.append(neighbor)
                        tentativeGScore=gScore[current[0]][current[1]]+1
                        if(tentativeGScore<gScore[neighbor[0]][neighbor[1]]):
                            cameFrom[neighbor]=current
                            gScore[neighbor[0]][neighbor[1]]=tentativeGScore
                            fScore[neighbor[0]][neighbor[1]]=gScore[neighbor[0]][neighbor[1]]+heuristic(neighbor,final)
            i+=1
    return False
def reconstruct_path(cameFrom,current):
    path=[current]
    while(current in cameFrom.keys()):
        current=cameFrom[current]
        path.append(current)
    return path

map=[[0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,1,0,0,0,0,0],
    [0,1,1,1,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]]
path=AStar(map,(0,0),(9,9),h)
#print(AStar(map,(0,0),(4,4),h))
#print(h((2,2),(4,4)))
for i in path:
    map[i[0]][i[1]]=7
for i in map:
    #print i
    pass
    