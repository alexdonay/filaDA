# Implementar as seguintes operações na classe ListaDuplamenteEncadeada:

# • Inserir no início à inserir_inicio() v
# • Inserir no final à inserir_final() v
# • Excluir do início à excluir_inicio()v
# • Excluir do final à excluir_final()v
# • Excluir da posição à excluir_posição()
# • Mostrar inicio à mostrar_inicio()
# • Mostrar final à mostrar_final()
class lista:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.last = None
        self.root = None
        self.fim = None

    def inserir_inicio(self, value):
        new = lista(value)
        if self.root == None:
            self.root = new
            self.fim = new
        else:
            self.root.last = new
            new.next = self.root
            self.root = new

    def inserir_final(self, value):
        aux = self.fim
        new = lista(value)
        self.fim = new
        self.fim.last = aux
        aux.next = self.fim

    def excluir_inicio(self):
        self.root = self.root.next
        self.root.last = None
    
    def excluir_final(self):
            self.fim = self.fim.last
            self.fim.next = None
    
    def excluir_posição(self,posicao):
        
        atual = self.root
        try:
            
            for i in range(posicao+1):
                print(f"posicao {posicao} indice {i}")
                if i == posicao:
                    atual.next = atual.next.next
                else:
                    atual = atual.next

            
        except:
            print("indice não encontrado")
            

    def __repr__(self):
        atual = self.root
        arr = ""
        while (atual != None):
            if atual.last == None:
                arr = str(atual.value)
            else:
                arr = arr + " - " + str(atual.value)
            atual = atual.next
        return arr


listaencadeada = lista()
listaencadeada.inserir_inicio(1)
listaencadeada.inserir_inicio(2)
listaencadeada.inserir_inicio(3)
listaencadeada.inserir_inicio(4)
listaencadeada.inserir_final(15)
listaencadeada.inserir_final(25)
listaencadeada.inserir_inicio(13)
print(listaencadeada)
listaencadeada.excluir_inicio()
print(listaencadeada)
listaencadeada.inserir_inicio(83)
print(listaencadeada)
listaencadeada.excluir_final()
listaencadeada.excluir_final()
print(listaencadeada)
listaencadeada.excluir_posição(0)
print(listaencadeada)
