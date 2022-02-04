'''Ana Paula Aguiar de Abreu - João Alves de Albuquerque Neto'''

import re

def _readproducts():
    products = []
    with open("artigos.txt", "r") as f:
        lines = f.read().split("\n")
        lines_s = [i.split() for i in lines]
        for i in lines_s:
            if i[3] == "s":
                products.append(ProductS(eval(i[0]), i[1], i[2], float(i[4])))
            else:
                products.append(ProductA(eval(i[0]), i[1], i[2], [i[4:]]))
        return products

class Store:
    def __init__(self, clients):
        self._clients = clients
        self._products = _readproducts()
    def getClients(self):
        return self._clients
    def getProducts(self):
        return self._products
    def getLastClient(self):
        cont = 0
        for n in self._clients:
            cont += 1
        return cont - 1
    def setPrice(self):
        for n in self._products:
            if isinstance(n, ProductA):
                n.setPrice(self._products)    
    def getClientByNum(self, numc):
        for n in self._clients:
            if n.getNum() == numc:
                return n
        return 0
    def setCreditClientByNum(self, numc, nv):
        for n in self._clients:
            if n.getNum() == numc:
                n.setCredito(nv)
    def setGastoClientByNum(self, num, gasto):
        for n in self._clients:
            if n.getNum() == num:
                n.setGasto(gasto + n.getGasto())
    def newClient(self, client):
        self._clients += [client]
    def listClients(self):
        for n in self._clients:
            print("Número de cliente : " + str(n.getNum()) + "| Tipo de Cliente" + n.getTipo() + "| Valor já comprado:" + str(n.getGasto()) + "\n")
    def listProducts(self, tipo):
        for n in self._products:
            if tipo == "l" and n.getTipo() == "l":
                if isinstance(n, ProductS):
                    print(str(n.getNum()) +" "+ n.getNome() + " " + n.getTipo() + " " + str(n.getPrice()))
                else:
                    print(str(n.getNum()) +" "+ n.getNome() + " " + n.getTipo() + " " + (' '.join(re.findall(r'[0-9]', n.getPrintList()))))
            elif tipo == "p" and (n.getTipo() == "l" or n.getTipo() == "p"):
                if isinstance(n, ProductS):
                    print(str(n.getNum()) +" "+ n.getNome() + " " + n.getTipo() + " " + str(n.getPrice()))
                else:
                    print(str(n.getNum()) +" "+ n.getNome() + " " + n.getTipo() + " " + (' '.join(re.findall(r'[0-9]', n.getPrintList()))))
            elif tipo == "o":
                if isinstance(n, ProductS):
                    print(str(n.getNum()) +" "+ n.getNome() + " " + n.getTipo() + " " + str(n.getPrice()))
                else:
                    print(str(n.getNum()) +" "+ n.getNome() + " " + n.getTipo() + " " + (' '.join(re.findall(r'[0-9]', n.getPrintList()))))           

class Carrinho:
    def __init__(self, client, products):
        self._client = client
        self._products = products
    def setNumClient(self, num):
        self._client = num
    def addProduct(self, product, store):
        cont = 0
        for n in store.getProducts():
            if n.getNum() == product:
                cont += 1
                self._products += [product]
        if cont == 1:
            print("Produto adicionado com sucesso!")
        else:
            print("Número de produto inválido!")
    def remProduct(self, product):
        cont = 0
        for n in self._products:
            if n == product:
                del(self._products[cont])
                print("Produto removido !")
                return
            cont += 1
        print("Produto não encontrado !")
    def getTotalBuy(self, store):
        value = 0
        for n in self._products:
            for m in store.getProducts():
                if n == m.getNum():
                    value += m.getPrice()
        return value
    def calcltype(self, store):
        if store.getClientByNum(self._client).getTipo() == "l":
            return "l"
        elif store.getClientByNum(self._client).getGasto() + self.getTotalBuy(store) > 1000:
            return "o"
        else:
            return "p"
    def listProducts(self, store):
        for m in self._products:
            for n in store.getProducts():
                if m == n.getNum():
                    if isinstance(n, ProductS):
                        print(str(n.getNum()) +" "+ n.getNome() + " " + n.getTipo() + " " + str(n.getPrice()))
                    else:
                        print(str(n.getNum()) +" "+ n.getNome() + " " + n.getTipo() + " " + (' '.join(re.findall(r'[0-9]', n.getPrintList()))))                     
                    
class Client:
    def __init__(self, num, tipo, gasto):
        self._num = num
        self._tipo = tipo
        self._gasto = gasto
        self._credito = 1500.0
    def getNum(self):
        return self._num
    def getTipo(self):
        return self._tipo
    def getGasto(self):
        return self._gasto
    def getCredito(self):
        return self._credito
    def setNum(self, num):
        self._num = num
    def setTipo(self, tipo):
        self._tipo = tipo
    def setGasto(self, gasto):
        self._gasto = gasto
    def setCredito(self, credito):
        self._credito = credito

class Product:
    def __init__(self, num, nome, tipo):
        self._num = num
        self._nome = nome
        self._tipo = tipo
    def getNum(self):
        return self._num
    def getNome(self):
        return self._nome
    def getTipo(self):
        return self._tipo
    def setNum(self, num):
        self._num = num
    def setTipo(self, tipo):
        self._tipo = tipo
    def setNome(self, nome):
        self._nome = nome      

class ProductS(Product):
    def __init__(self, num, nome, tipo, price):
        super().__init__(num, nome, tipo)
        self._price = price
    def getPrice(self):
        return self._price

class ProductA(Product):
    def __init__(self, num, nome, tipo, listnum):
        super().__init__(num, nome, tipo)
        self._listnum = listnum
        self._price = 0;
    def getList(self):
        return self._listnum
    def getPrintList(self):
        nlist = ""
        for n in self._listnum:
            nlist += str(n) + " "
        return nlist
    def setPrice(self, products):
        value = 0
        for m in self._listnum:
            for n in products:
                if n.getNum() == m:
                    value += n.getPrice()
        self._price = value
    def getPrice(self):
        return self._price

    
def printinitst():
        print("\n==========================")
        print("===== Menu de venda ======")
        print("==========================")
        print("1 - Tipo de cliente")
        print("2 - Listar artigos")
        print("3 - Adicionar artigos ao carrinho")
        print("4 - Retirar artigos ao carrinho")
        print("5 - Ver compras no carrinho")
        print("6 - Ver credito disponivel")
        print("7 - Saldar credito")
        print("8 - Finalizar a venda")
        print("0 - Sair\n")   
        
def initstore(store, numclient):
        produtos = []
        carrinho = Carrinho(numclient, produtos)
        button = 1
        while button != 0:
            printinitst()
            button = eval(input("Escolha um número = "))            
            if button == 1:
                print(store.getClientByNum(numclient).getTipo())
            elif button == 2:
                store.listProducts(carrinho.calcltype(store))              
            elif button == 3:
                adp = eval(input("Digite o número do artigo que pretende adicionar ao carrinho = "))
                carrinho.addProduct(adp, store)
            elif button == 4:
                adp = eval(input("Digite o número do artigo que pretende retirar do carrinho = "))
                carrinho.remProduct(adp)
            elif button == 5:
                if carrinho.getTotalBuy(store) == 0:
                    print("Seu carrinho está vazio.")
                else: 
                    carrinho.listProducts(store)
            elif button == 6:
                if store.getClientByNum(numclient).getTipo() == "o":
                        print("Crédito Disponível : " + str(store.getClientByNum(numclient).getCredito()))
                else:
                    print("Sem crédito disponível !")
            elif button == 7:
                if store.getClientByNum(numclient).getTipo() == "o":
                    store.setCreditClientByNum(numclient, 1500.0)                    
                    print("Crédito Saldado ! \n Novo Disponível : " + str(store.getClientByNum(numclient).getCredito()))
                else:
                    print("Sem crédito disponível !")
            elif button == 8:
                if carrinho.getTotalBuy(store) == 0:
                    print("Seu carrinho está vazio !")                
                elif store.getClientByNum(numclient).getTipo() == "l":
                    nc = eval(input("Pretende efetuar cadastro ? \n 1 - Sim \n 2 - Não\n"))
                    if nc == 1:
                        nclient = Client(store.getLastClient() + 1, carrinho.calcltype(store), 0)
                        if carrinho.calcltype(store) == "o":
                            payment = eval(input("1 - Pagar no crédito \n 2 - Pagar no débito \n"))
                            if payment == 1:
                                if store.getClientByNum(numclient).getCredito() > (carrinho.getTotalBuy(store)*0.9):
                                    store.setCreditClientByNum(numclient, store.getClientByNum(numclient).getCredito() - round(carrinho.getTotalBuy(store)*0.9, 2))
                                    print("Seu número de cliente é "+ str(nclient.getNum()) + " compra efetuada no montante de "+ str(carrinho.getTotalBuy(store)) + "descontos no montante de " + str(round(carrinho.getTotalBuy(store)-(carrinho.getTotalBuy(store)*0.9), 2)) + " valor total da compra de " + str(round(carrinho.getTotalBuy(store)*0.9, 2)))
                                    carrinho.listProducts(store)
                                    nclient.setTipo("o")
                                    store.newClient(nclient)
                                    produtos = []
                                    numclient = nclient.getNum()
                                    carrinho = Carrinho(numclient, produtos)                                    
                                else:
                                    print("Saldo em crédito insuficiente !")
                                    store.newClient(nclient)
                                    nclient.setTipo("p")
                                    carrinho.setNumClient(nclient.getNum(), produtos)
                            else:
                                nclient.setGasto(round(carrinho.getTotalBuy(store)*0.9, 2))
                                nclient.setTipo("o")
                                store.newClient(nclient)
                                print("Seu número de cliente é "+ str(nclient.getNum()) + " compra efetuada no montante de "+ str(carrinho.getTotalBuy(store)) + "descontos no montante de " + str(round(carrinho.getTotalBuy(store)-(carrinho.getTotalBuy(store)*0.9), 2)) + " valor total da compra de " + str(round(carrinho.getTotalBuy(store)*0.9, 2)))
                                carrinho.listProducts(store)
                                produtos = []
                                numclient = nclient.getNum()
                                carrinho = Carrinho(numclient, produtos)                            
                        else:
                            print("Seu número de cliente é "+ str(nclient.getNum()) + " compra efetuada no montante de "+ str(carrinho.getTotalBuy(store)) + " descontos no montante de " + str(round(carrinho.getTotalBuy(store)-(carrinho.getTotalBuy(store)*0.95), 2)) + " valor total da compra de " + str(round(carrinho.getTotalBuy(store)*0.95, 2)))
                            nclient.setGasto(round(carrinho.getTotalBuy(store)*0.95, 2))
                            carrinho.listProducts(store)
                            nclient.setTipo("p")
                            store.newClient(nclient)
                            produtos = []
                            numclient = nclient.getNum()
                            carrinho = Carrinho(numclient, produtos)                             
                    else:        
                        print("Sua compra foi efetuada no montante de "+ str(carrinho.getTotalBuy(store)) + " descontos no montante de 0.0 valor total da compra de " + str(carrinho.getTotalBuy(store)))
                        produtos = []
                        carrinho = Carrinho(numclient, produtos)
                elif carrinho.calcltype(store) == "p":
                    print("Seu número de cliente é "+ str(numclient) + " compra efetuada no montante de "+ str(carrinho.getTotalBuy(store)) + " descontos no montante de " + str(round(carrinho.getTotalBuy(store)-(carrinho.getTotalBuy(store)*0.95), 2)) + " valor total da compra de " + str(round(carrinho.getTotalBuy(store)*0.95, 2)))
                    store.setGastoClientByNum(numclient, round(carrinho.getTotalBuy(store)*0.95, 2))
                    carrinho.listProducts(store)
                    produtos = []
                    carrinho = Carrinho(numclient, produtos)                    
                else:
                    payment = eval(input("1 - Pagar no crédito \n 2 - Pagar no débito \n"))
                    if payment == 1:
                        if store.getClientByNum(numclient).getCredito() > (carrinho.getTotalBuy(store)*0.9):
                            store.setCreditClientByNum(numclient, store.getClientByNum(numclient).getCredito() - round(carrinho.getTotalBuy(store) * 0.9, 2))
                            print("Seu número de cliente é "+ str(numclient) + " compra efetuada no montante de "+ str(carrinho.getTotalBuy(store)) + " descontos no montante de " + str(round(carrinho.getTotalBuy(store)-(carrinho.getTotalBuy(store)*0.9),2)) + " valor total da compra de " + str(round(carrinho.getTotalBuy(store)*0.9, 2)))
                            carrinho.listProducts(store)
                            produtos = []
                            carrinho = Carrinho(numclient, produtos)                                    
                        else:
                            print("Saldo em crédito insuficiente !")
                            store.newClient(nclient)
                            carrinho.setNumClient(nclient.getNum(), produtos)
                    else:
                        store.setGastoClientByNum(numclient, round(carrinho.getTotalBuy(store)*0.95, 2))
                        print("Seu número de cliente é "+ str(numclient) + " compra efetuada no montante de "+ str(carrinho.getTotalBuy(store)) + " descontos no montante de " + str(round(carrinho.getTotalBuy(store)-(carrinho.getTotalBuy(store)*0.9), 2)) + " valor total da compra de " + str(round(carrinho.getTotalBuy(store)*0.9, 2)))
                        carrinho.listProducts(store)
                        produtos = []
                        carrinho = Carrinho(numclient, produtos)

def initialfunc(store):
    button = 1
    while button != 0:
        print("1 - Login")
        print("2 - Listar Clientes")
        print("0 - Sair")
        button = eval(input())
        if button == 1:
            nc = eval(input("Escreva o número do cliente: \n(Caso não tenha registo, escreva o número 0)\n"))
            if store.getClientByNum(nc) != 0:
                initstore(store, nc)
            else:
                print("Número de cliente não encontrado !")
        elif button == 2:
            store.listClients()
            
firstclient = Client(0, "l", 0)
clients = [firstclient]
store = Store(clients)

initialfunc(store)
