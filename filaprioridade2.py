class fila:
    def __init__(self, arr=None) -> None:
        self.arr = []
        self.tamanho = 0
        self.indexInicial = 0
        self.indexFinal = 0
        if arr != None:
            for i in arr:
                self.append(i["prioridade"], i["dado"])

    def __str__(self) -> str:
        result = ""
        for i in range(self.indexInicial, self.indexFinal):
            item = self.arr[i]
            if i == self.indexInicial:
                result = item
            else:
                result = str(result) + "," + str(item)
        return "[" + str(result) + "]"

    def append(self, prioridade, dado):
        self.indexFinal += 1
        self.arr.append({"prioridade": prioridade, "dado": dado})
        proximoItem = {"prioridade": prioridade, "dado": dado}
        for i in range(self.indexFinal-1):
            itemAtual = self.arr[i]
            if itemAtual["prioridade"] > proximoItem["prioridade"]:
                self.arr[i] = proximoItem
                proximoItem = self.arr[i+1]
                self.arr[i+1] = itemAtual

    def remove(self):
        if self.indexFinal != self.indexInicial:
            self.indexInicial += 1
        else:
            raise Exception("Fila vazia")
        return self.arr[self.indexInicial-1]


nova = fila([{"prioridade": 3, "dado": "estudar"}, {
            "prioridade": 2, "dado": "trabalhar"}])

nova.append(5, "jogar")
nova.append(1, "Play")
print(nova)
print(nova.remove())
print(nova.remove())
print(nova)
