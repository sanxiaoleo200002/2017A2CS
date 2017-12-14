#Leo Qiu Opt3
nullPointer = -1

class Node:
    def __init__(self):
        self.Data = ""
        self.nextPointer = nullPointer

class Queue:
    def __init__(self):
        self.startPointer = nullPointer      
        self.freePointer = 0
        self.record = []
        newNode = None
        
        for i in range(10):
            newNode = Node()
            newNode.nextPointer = i + 1
            self.record.append(newNode)
        newNode.nextPointer = nullPointer        
        
    def enqueue(self, newItem):
        if self.freePointer != nullPointer:
            newPointer = self.freePointer
            self.record[newPointer].Data = newItem
            self.record[newPointer].nextPointer = nullPointer
            for i in range(10):
                if (self.record[i].nextPointer == nullPointer) and (self.record[i].Data != None):
                    self.record[i].nextPointer = newPointer
                    self.freePointer = self.freePointer + 1

    def dequeue(self):
        freeone = self.freePointer
        if self.record[self.startPointer].Data != None:
            self.record[self.startPointer].nextPointer = self.freePointer
            currentPointer = self.record[self.startPointer].nextPointer
            return(self.record[self.startPointer].Data)
            self.freePointer = self.startPointer
            self.startPointer = currentPointer
  
