import LisctaCircular as Circular

class Tarea2():
    def __init__(self):
        lcircular = Circular.Circular()
        n = 0
        while n <= 4:
            numero = int(input("Ingrese un Numero: "))
            lcircular.insertar(Circular.CicularNodo(numero))
            n =n+1
        bnumero = int(input("Numero a buscar: "))
        lcircular.imprimir(bnumero)

def main():
    Tarea2()


if __name__ == '__main__':
   main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
