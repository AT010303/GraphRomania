from graph import *

class node:
    def __init__(self,name,parent,Depth):
        self.name = str(name)
        self.hn = int(heuristic.get(name))
        self.parent = parent
        self.Depth = Depth
        if parent != None:
            self.path = parent.path + [name]
            map = romania_map.get(parent.name)
            self.gn = int(parent.gn) + int(map.get(self.name))
            self.fn = self.hn + self.gn
        else:
            self.path = [name]
            self.fn = int(self.hn)
            self.gn = 0

    def Print(self):
        print(self.name,self.gn,self.hn,self.fn)
        print(self.path)
        print(self.Depth)

    def explore(self):
        M = []
        map = romania_map.get(self.name)
        M = list(map.keys())
        return M