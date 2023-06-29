
class priorityQueue:
    def __init__(self):
        self.queue = []
    def push(self,obj,cost):
        self.queue.append((cost,obj))
        self.queue.sort()
    def pop(self):
        return self.queue.pop(0)
    def Print(self):
        print(self.queue)