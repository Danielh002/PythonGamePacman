def checkVF(map,inicial,final):
    if(map[final[0]][final[1]]==1   or map[inicial[0]][inicial[1]]):
        return False
    res=[]
    i=0
    if(inicial[0]==final[0]):
        if(inicial[1]>final[1]):
            while(inicial[1]-i>final[1]):
                if(map[inicial[0]][inicial[1]-i]==1):
                    return False
                res.insert(0,(inicial[0],inicial[1]-i))
                i+=1
        else:
            while(inicial[1]+i<final[1]):
                if(map[inicial[0]][inicial[1]+i]==1):
                    return False
                res.insert(0,(inicial[0],inicial[1]+i))
                i+=1
    elif(inicial[1]==final[1]):
        if(inicial[0]>final[0]):
            while(inicial[0]-i>final[0]):
                if(map[inicial[0]-i][inicial[1]]==1):
                    return False
                res.insert(0,(inicial[0]-i,inicial[1]))
                i+=1
        else:
            while(inicial[0]+i<final[0]):
                if(map[inicial[0]+i][inicial[1]]==1):
                    return False
                res.insert(0,(inicial[0]+i,inicial[1]))
                i+=1
    else:
        return False
    return [final]+res


map=[[0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [1,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0]]
print(checkVF(map,(5,0),(0,0)))