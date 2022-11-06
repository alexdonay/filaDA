class pilhaCustomizada:

    def __init__(self, tamanho, tipoAux):
        self.tipo = self.type(tipoAux)
        self.pilha = [self.tipo for i in range(tamanho)]
        self.topo = 0
        self.tamanho = tamanho

    def type(self, tipo):
        if tipo == "I":
            return 0
        if tipo == "F":
            return 0.0
        if tipo == "S":
            return ""
        else:
            print("caractere inválido")

    def verificaCheia(self):
        if self.tamanho == self.topo:
            return True
        else:
            return False

    def verificaVazia(self):
        if self.tamanho == 0:
            return True
        else:
            return False

    def empilhar(self, valor):
        if (self.verificaCheia() == False and type(valor) == type(self.tipo)):
            self.pilha[self.topo] = valor
            self.topo += 1
        else:
            print(f"{valor}  do tipo {type(valor)} esta fora do range ou valor é")

    def desempilhar(self):
        if self.verificaVazia() == False:
            self.topo -= 1
        else:
            print("Não existem dados a serem removidos")

    def toString(self):

        return self.pilha[0:self.topo]


c = pilhaCustomizada(9, "I")
c.empilhar(2)
c.empilhar(3)
c.empilhar('0')
print(c.toString())
