def distance(i,j):
    return ((i.posX-j.posX)**2+(i.posY-j.posY)**2)**(1/2.0)
def normalize(v):
    dv=(v[0]**2+v[1]**2)**(1/2.0)
    if(dv!=0):
        return([v[0]/dv,v[1]/dv])
    else:
        return([0,0])
class flocking():
    def __init__(self,agents):
        self.agents=agents
        self.resultAlignaments=None
        self.resultCohesion=None
        self.resultSeparation=None
        self.distanceFlocking=1000
        self.alignamentWeight=1
        self.cohesionWeight=5
        self.separationWeigth=3
    def computeAlignaments(self):
        # velocity
        res=[]
        for i in self.agents:
            v=[0,0]
            neighborCount=0
            for j in self.agents:
                if(i!=j and distance(i,j)<self.distanceFlocking):
                    v[0]+=j.velX
                    v[1]+=j.velY
                    neighborCount+=1
            if(neighborCount>0):
                v[0]/=neighborCount
                v[1]/=neighborCount
                v=normalize(v)
            res.append(v)
        self.resultAlignaments=res
    def computeCohesion(self):
        res=[]
        for i in self.agents:
            v=[0,0]
            neighborCount=0
            for j in self.agents:
                if(i!=j and distance(i,j)<self.distanceFlocking):
                    v[0]+=j.posX
                    v[1]+=j.posY
                    neighborCount+=1
            if(neighborCount>0):
                v[0]/=neighborCount
                v[1]/=neighborCount
                v=[v[0]-i.posX,v[1]-i.posY]
                v=normalize(v)
            res.append(v)
        self.resultCohesion=res
    def computeSeparation(self):
        res=[]
        for i in self.agents:
            v=[0,0]
            neighborCount=0
            for j in self.agents:
                if(i!=j and distance(i,j)<self.distanceFlocking):
                    v[0]+=j.posX-i.posX
                    v[1]+=j.posY-i.posY
                    neighborCount+=1
            if(neighborCount>0):
                v[0]/=neighborCount
                v[1]/=neighborCount
                v=[v[0]-i.posX,v[1]-i.posY]
                v=normalize(v)
                v=[v[0]*-1,v[1]*-1]
            res.append(v)
        self.resultSeparation=res
    def copyAlignaments(self):
        i=0
        while(i<len(self.agents)):
            if(type(self.agents[i]).__name__=="LitleGhost"):
                self.agents[i].velX=self.resultAlignaments[i][0]
                self.agents[i].velY=self.resultAlignaments[i][1]
            i+=1
    def copyComputation(self):
        i=0
        while(i<len(self.agents)):
            if(type(self.agents[i]).__name__=="LitleGhost"):
                v=[0,0]
                v[0]=self.resultAlignaments[i][0]*self.alignamentWeight+self.resultCohesion[i][0]*self.cohesionWeight+self.resultSeparation[i][0]*self.separationWeigth
                v[1]=self.resultAlignaments[i][1]*self.alignamentWeight+self.resultCohesion[i][1]*self.cohesionWeight+self.resultSeparation[i][1]*self.separationWeigth
                v=normalize(v)
                self.agents[i].velX+=v[0]
                self.agents[i].velY+=v[1]
                aux=[self.agents[i].velX,self.agents[i].velY]
                self.agents[i].velX,self.agents[i].velY=normalize(aux)
            i+=1
class agent():
    def __init__(self,x,y,vx,vy):
        self.posX=x
        self.posY=y
        self.velX=vx
        self.velY=vy

if(__name__=="__main__"):
    agents=[]
    agents.append(agent(2,2,1.4,1.3))
    agents.append(agent(2,3,1.4,1.2))
    agents.append(agent(2,4,1.4,1.3))
    agents.append(agent(2,5,1.4,1.4))
    agents.append(agent(3,2,1.5,1.2))
    f=flocking(agents)
    f.computeAlignaments()
    f.computeCohesion()