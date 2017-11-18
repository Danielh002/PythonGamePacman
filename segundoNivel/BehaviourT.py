class BehaviourT ():
    def __init__(self,typeNode=None,fun=None,params=None):
        self.root=[]
        self.typeNode=typeNode
        self.fun=fun
        self.params=params
    def addTree(self,tree):
        self.root.append(tree)
    def runTree(self):
        if(self.typeNode=="root"):
            for i in self.root:
                i.runTree()
        elif(self.typeNode=="seq"):
            for i in self.root:
                if(not i.runTree()):
                    return False
            return True
        elif(self.typeNode=="select"):
            for i in self.root:
                if(i.runTree()):
                    return True
            return False
        else:
            return(self.fun(self.params))
def hola(params):
    print("hola mundo "+params[0])
    return params[1]   
if(__name__=="__main__"):
    tree=BehaviourT("root")
    b=BehaviourT("seq")
    b.addTree(BehaviourT(None,hola,("nose 1",False)))
    b.addTree(BehaviourT(None,hola,("nose 2",False)))
    b.addTree(BehaviourT(None,hola,("nose 3",True)))
    b.addTree(BehaviourT(None,hola,("nose 4",False)))
    b.addTree(BehaviourT(None,hola,("nose 5",True)))
    c=BehaviourT("select")
    c.addTree(BehaviourT(None,hola,("nose 1",False)))
    c.addTree(BehaviourT(None,hola,("nose 2",False)))
    c.addTree(BehaviourT(None,hola,("nose 3",True)))
    c.addTree(BehaviourT(None,hola,("nose 4",False)))
    c.addTree(BehaviourT(None,hola,("nose 5",True)))
    tree.addTree(b)
    tree.addTree(c)
    tree.runTree()