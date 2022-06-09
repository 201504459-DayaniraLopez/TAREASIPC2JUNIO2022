class CicularNodo:
    def __init__(self, Numero):
        self.numero = Numero
        self.siguiente = None
        self.anterior = None


class Circular:
    def __init__(self):
        self.inicio = None
        self.final = None

    def insertar(self, dato):
        if self.inicio == None:
            self.inicio = self.final = dato
        else:
            aux = self.final
            self.final = aux.siguiente = dato
            self.final.anterior = aux
        self.__unir_nodos()

    def __unir_nodos(self):
        if self.inicio   != None:
            self.inicio.anterior = self.final
            self.final.siguiente = self.inicio

    def imprimir(self, dato):
        aux = self.inicio
        while aux:
            if aux.numero == dato:
                print("Anterior:" + str(aux.anterior.numero))
                print("Actual: " + str(aux.numero))
                print("Siguiente: " + str(aux.siguiente.numero))
                break
            else:
                aux = aux.siguiente
                if aux == self.inicio:
                    return False

