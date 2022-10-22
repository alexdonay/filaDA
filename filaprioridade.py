class filaPrioritaria:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.arr =[]
    
    def isEmpty(self):
        return self.arr == []
    
    def isFull(self):
        return len(self.arr) == self.tamanho
    
    def append(self,value):
        if not self.isFull():
            self.arr.append(value)
        else:
            raise Exception("A fila está cheia")
    def remove(self):
        max = 0
        if not self.isEmpty():
            for i in range(len(self.arr)):
                if self.arr[i] > self.arr[max] : max = i
            number = self.arr[max]
            del(self.arr[max])
            return number
        raise Exception("Fila vazia")
        
fil = filaPrioritaria(3)


fil.append(3)
fil.append(7)
fil.append(5)
print(fil.arr)
print(fil.remove())
print(fil.arr)


        