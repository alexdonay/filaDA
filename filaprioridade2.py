class fila:
    def __init__(self, arr=None) -> None:
        self.arr = []
        if arr != None:
            for i in arr:
                self.append(i["prioridade"], i["dado"])

    def __str__(self) -> str:
        result = ""
        for i in range(len(self.arr)):
            item = self.arr[i]
            if result == "":
                result = str(item)
            else:
                result = str(result) + "," + str(item)
        return "[" + str(result) + "]"

    def append(self, prioridade, dado):
        novo = {"prioridade": prioridade, "dado": dado}
        for i in range(len(self.arr)):
            atual = self.arr[i]
            if atual["prioridade"] > novo["prioridade"]:
                self.arr[i] = novo
                novo = atual
        self.arr.append(novo)

    def remove(self):
        arrAux = []
        retirado = self.arr[0]
        for i in range(1, len(self.arr)):
            arrAux.append(self.arr[i])
        self.arr = arrAux
        return retirado


nova = fila([{"prioridade": 3, "dado": "estudar"}])
nova.append(1, "estudar")
nova.append(4, "viajar")
nova.append(2, "trabalhar")
print(nova.remove())
print(nova)
