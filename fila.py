class Fila:
    def __init__(self):
        self.itens = []

    def isEmpty(self):
        return self.itens == []
    
    def enfileirar(self, item):
        self.itens.insert(0, item)
    
    def desenfileirar(self):
        if(self.isEmpty()):
            pass
        else:
            return self.itens.pop()
    
    def tamanho(self):
        return len(self.itens)