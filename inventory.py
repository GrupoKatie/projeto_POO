from UI import *
from categorias.alimento import Alimento
from categorias.papelaria import Papelaria
from categorias.bebida import Bebida

class Inventory:
    def __init__(self):
        self.arr = []
        self.index = 0
        pass

    def addProduct(self):
        str_input = "Insira a categoria do produto: " + PRODUCT_OPTIONS + "Opção: "
        category = int(input(str_input))

        if category == 1:
            p = Alimento(input("Peso: "), input("Tipo: "), input("Nome: "), input("Preço: "), input("Data de Validade: "), input("Marca: "), self.index, input("Quantidade: "), input("Data de Adição: "), input("É transgenico (True/False)?"))
        elif category == 2:
            p = Bebida(input("Volume: "), input("Tipo: "), input("Nome: "), input("Preço: "), input("Data de Validade: "), input("Marca: "), self.index, input("Quantidade: "), input("Data de Adição: "), input("É alcoólico (True/False)?"))
        elif category == 3:
            p = Papelaria(input("Cor: "), input("Tipo: "), input("Nome: "), input("Preço: "), input("Data de Validade: "), input("Marca: "), self.index, input("Quantidade: "), input("Data de Adição: "), input("É reciclável (True/False)?"))
        
        if category in [1, 2, 3]:
            self.index += 1
            self.arr.append(p)
        else: print(ERROR_MESSAGE)

    def changeProduct(self):
        id = int(input("Insira o ID do produto a ser modificado:\n"))

        for pd in self.arr:
            if pd.ID == id:
                index = self.arr.index(pd)
                self.updateData(index)
                return
        print(NOT_FOUND)

    def removeProduct(self):
        id_to_remove = int(input("Insira o ID que deseja remover:"))

        for p in self.arr:
            if p.ID == id_to_remove:    
                self.arr.remove(p)
                return
        print(NOT_FOUND)    

    def updateData(self, index):

        class_name = self.arr[index].__class__.__name__

        str_input = "Selecione uma opção para mudança: " + PRODUCT_CHANGE_OPTIONS + PRODUCT_CHANGE_OPTIONS_SPEC[class_name]
        
        option = input(str_input)
        data = input("Insira o novo dado: ") 
        self.arr[index].updateData(option.lower(), data)
        
    def generalChange(self, index, option):
        if option == 1:
            self.arr[index].name = input("Insira o novo dado: ") 
        elif option == 2:
            self.arr[index].price = input("Insira o novo dado: ") 
        elif option == 3:
            self.arr[index].expiration_date = input("Insira o novo dado: ") 
        elif option == 4:
            self.arr[index].brand = input("Insira o novo dado: ") 
        elif option == 5:
            self.arr[index].amount = input("Insira o novo dado: ") 
    
    def reportCategory(self):
        str_input = "Insira a categoria para listar:" + PRODUCT_OPTIONS
        category = int(input(str_input))
        categories = {1: Alimento, 2: Bebida, 3: Papelaria}
        
        print("Produtos da categoria selecionada:\n")

        for p in self.arr:
            if isinstance(p, categories[category]):
                print(p)

    def reportExpiration(self):
        print("Produtos com menos de um mês de validade: ")
        for p in self.arr:
            if p.isNearExpiration():    
                print(p)
