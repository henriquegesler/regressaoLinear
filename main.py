import numpy as np
import matplotlib.pyplot as plt

class Cidade():
    def __init__(self, populacao, lucro):
        self.populacao = populacao
        self.lucro = lucro

f = open("data1.txt", "r")
lines = f.readline()
x=0
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
    cid = Cidade(float (pop),float (luc))
    cidades.append(cid)
    print(cidades[x].populacao)
    print(cidades[x].lucro)
    x+=1
    lines = f.readline()

#print(len(cidades))
for a in range(len(cidades)): #para cada valor do meu array, plota um x e y
    plt.plot(cidades[a].populacao, cidades[a].lucro, 'rx')  # x vermelho
plt.axis([4, 24, -5, 25])
plt.title("Regressão Linear")
plt.grid(True)
plt.xlabel("Population 10.000s")
plt.ylabel("Lucro 10.000s")
plt.show()