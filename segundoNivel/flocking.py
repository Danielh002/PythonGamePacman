def distance(i,j):
    return ((i.posX-j.posX)**2+(i.posY-j.posY)**2)**(1/2.0)
class flocking():
    def __init__(self,agents):
        self.agents=agents
    def computeAlignaments(self):
        # velocity
        res=[]
        for i in self.agents:
            v=[0,0]
            neighborCount=0
            for j in self.agents:
                if(i!=j and distance(i,j)<100):
                    v[0]+=j.velX
                    v[1]+=j.velY
                    neighborCount+=1
            if(neighborCount>0):
                v[0]/=neighborCount
                v[1]/=neighborCount
                #faltaNormalizar
            res.append(v)
        print res
    def computeCohesion(self):
        res=[]
        for i in self.agents:
            v=[0,0]
            neighborCount=0
            for j in self.agents:
                if(i!=j and distance(i,j)<100):
                    v[0]+=j.posX
                    v[1]+=j.posY
                    neighborCount+=1
            if(neighborCount>0):
                v[0]/=neighborCount
                v[1]/=neighborCount
                #v = new Point(v.x - myAgent.x, v.y - myAgent.y);
                #faltaNormalizar
            res.append(v)
        print res
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