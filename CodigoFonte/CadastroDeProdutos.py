
#Classe que manuseia produtos
class Produto:
    
    def __init__(self, codigo, nome, quantia,marca, custo_pu):
        self.__codigo = codigo
        self.__nome = nome
        self.__quantia = quantia
        self.__marca = marca
        self.__custo_pu = custo_pu  #custo por unidade


    def show(self):
        print("\n------------------------")
        print("Cód.:",  self.__codigo)
        print("Nome:", self.__nome)
        print("Quantidade:", self.__quantia)
        print("Marca: ", self.__marca)
        print("Valor de custo:", self.__custo_pu)


    #--------------GETTERS---------------
    def getCodigo(self):
        return self.__codigo

    def getNome(self):
        return self.__nome

    def getQuantia(self):
        return self.__quantia
    
    def getMarca(self):
        return self.__marca

    def getCusto(self):
        return self.__custo_pu


    #-------------SETTERS------------------
    def setCodigo(self, codigo):
        self.__codigo = codigo
    
    def setNome(self, nome):
        self.__nome = nome

    def setQuantia(self, quantia):
        self.__quantia = quantia

    def setMarca(self, marca):
        self.__marca = marca

    def setCusto(self, custo):
        self.__custo_pu = custo




class Estoque:
    #Lista de produtos
    __produtos = []
    __counter = 0

    #def __init__(self):
        
    #retorna o numero atual de produtos
    def getCounter(self):
        return self.__counter

    #retorna None se não encontrar
    #À implementar....por enquanto, busca linear
    def pesquisar(self, nome):
        for i in self.__produtos:
            if i.getNome() == nome:
                return i
        return None

    
    #Cadastra um novo produto na lista
    def cadastrar(self,produto):

        if isinstance(produto, Produto):
            if self.pesquisar(produto.getNome()) == None:

                self.__produtos.append(produto)
                self.__counter += 1
            else:
                print('Produto previamente cadastrado!')
        else:
            print('Erro! Objeto não é um Produto!\n')
            

    #Dá baixa de entrada, ou saida de 'qt' objetos cujo nome seja 'nome'
    #'qt' positivo para entradas, negativo para saídas.
    def baixaES(self, nome, qt):

        obj = pesquisar(nome)
        if obj!= None:
            new_qt = obj.getQuantia()+qt

            if new_qt >= 0:
                obj.setQuantia(new_qt)
            else:
                print('Impossível! estoque insuficiente!')
        else:
            print('Produto não cadastrado!')


    #Exibe uma lista básica
    def show(self):
        print('\n+------+--------------------+')
        print('|Codigo|           Produtos |')
        print('+------+--------------------+')

        for i in self.__produtos:
            print(str(i.getCodigo())+'|           '+i.getNome())
        print('\n--------------------------')

    #Dá um print na tela de todo o estoque
    def show_all(self):
        for i in self.__produtos:
            i.show()
            


    



        
class Main:
    def __init__(self):
        self.__es = Estoque()



    def Start(self):
        while True:
            entrada = input("\n1. Cadastrar produto\n2. Consultar produto\n3. Controle de estoque\n4. Sair\n-->")

            if entrada == '1':
                self.readProduct()

            elif entrada == '2':
                self.__es.show()

            elif entrada == '3':
                print('A implementar')
                break
            else:
                print('A implementar')
                break

    #Lê dados do teclado para o cadastro de um produto. 
    #Faltam a leitura de + dados
    def readProduct(self):
          while True:

            print("-------------------------")
            nome = input("Digite o nome do produto: ")

            if(nome == ""):
                print("\n--------------")
                print("Nome inválido!")
                print("--------------\n")

             #Se produto ja estiver condito na lista
            elif self.__es.pesquisar(nome) != None:

                print("\n------------------------------------")
                print("Nome ja cadastrado, tente novamente!")
                print("------------------------------------\n")

            else:
                quantia = input("Digite uma quantia: ")
                marca = input("Digite a marca do produto: ")
                custo = input("Digite o custo do produto: ")

                self.__es.cadastrar(Produto(self.__es.getCounter(), nome, quantia, marca, custo))
                break


m = Main()
m.Start()
            
