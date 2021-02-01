import matplotlib.pyplot as plt
import random

class Cidade():
    def __init__(self, populacao, lucro):
        self.populacao = populacao
        self.lucro = lucro

f = open("data1.txt", "r")
lines = f.readline()
#x=0
cidades = []
while (lines != ""):
    size = len(lines)
    for i in range(size):
        if lines[i]==",":
            pop = lines[0:i]
            #print((pop))
            marc=i
        if lines[i]=="\n":
            luc = lines[marc+1:i]
            #print((luc))
    cid = Cidade(float (pop),float (luc)) #cria o objeto cidade e transforma a string lida em um float diretamente
    cidades.append(cid)
    #print(cidades[x].populacao)
    #print(cidades[x].lucro)
    #x+=1
    lines = f.readline()
#print(len(cidades))

#A partir daqui começa o código de regressao linear
import numpy as np
rng = np.random.default_rng()
delta = 10 - 20*rng.random((2,)) #gera dois numeros de x a -x
print(delta)
alfa = 0.01
erroG = []
erroQ = []
g = 0
gMax = 25
#Enquanto for menos de 1k de gerações ou o erro não for igual a 0
while (g<gMax or erro==0):
    erroG.append(0)
    erroQ.append(0)
    #Função para misturar a lista
    random.shuffle(cidades)
    # For que realiza a operação da obtenção dos valores
    for a in range(len(cidades)):
        yObt = delta[0] + delta[1]*cidades[a].populacao
        #print(yObt, a)
        #print(cidades[a].lucro, a)
        erro = yObt - cidades[a].lucro
        erroG[g] = erroG[g]+erro
        erroQ[g] = erroQ[g]+(erro*erro)
        #print(erroG[g], erroQ[g])
        if (a%96 == 0 and a!=0):
            # Realizamos o ajuste dos deltas
            del0 = delta[0] - (alfa * (1 / len(cidades)) * erroG[g])
            del1 = delta[1] - (alfa * (1 / len(cidades)) * erroG[g] * cidades[a].populacao)
            delta[0] = del0
            delta[1] = del1
            print(delta, a, g)
    g += 1
a=0
print(erroG)
for a in range(gMax):
    plt.plot(a+1, erroG[a], 'rx')
plt.show()

#A partir daqui começa o gráfico
for a in range(len(cidades)): #para cada valor do meu array, plota um x e y
    plt.plot(cidades[a].populacao, cidades[a].lucro, 'rx')  # x vermelho
    yL = (delta[0]+(delta[1]*cidades[a].populacao))
    plt.plot(cidades[a].populacao, yL, 'bx')
plt.axis([4, 24, -5, 25])
plt.title("Regressão Linear")
plt.grid(True)
plt.xlabel("Population 10.000s")
plt.ylabel("Lucro 10.000s")
plt.show()