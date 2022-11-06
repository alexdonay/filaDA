class filaPrioritaria:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.quantElementos = 0
        self.arr =[]
        self.dados =[]
    
    def isEmpty(self):
        return self.quantElementos == 0
    
    def isFull(self):
        return self.quantElementos == self.tamanho
    
    def append(self,value,dados):
        if not self.isFull():
            self.arr.append(value)
            self.dados.append(dados)
            self.quantElementos += 1
        else:
            raise Exception("A fila está cheia")
    def remove(self):
        max = 0
        if not self.isEmpty():
            for i in range(len(self.arr)):
                if self.arr[i] > self.arr[max] : max = i
            number = self.dados[max]
            self.delete(self.arr, self.arr[max])
            self.delete(self.arr, self.dados[max])
            self.quantElementos -=1
            return number
        raise Exception("Fila vazia")
    
    def delete(self,arr, value):
        for i in range(len(arr)):
            if arr[i] == value :
                arr[i] = arr[i+1]
        arr[len(arr)-1] = 0;
        return arr



fil = filaPrioritaria(3)


fil.append(3,"Alexsander")
fil.append(7,"donay")
fil.append(5,"x9")
print(fil.arr)
print(fil.remove())
print(fil.arr)
print(fil.remove())
print(fil.arr)


