import csv
import algoritimoHierholzer as hierh

totNos = -1
vetNos = []

with open('data/nodes.csv', 'r') as ficheiro:
    reader = csv.reader(ficheiro)
    for linha in reader:
        if totNos == -1:
            totNos += 1 #Desconsidera a primeira linha
        else:
            totNos += 1
            vetNos.append(linha[0])

print("TOTAL DE VERTICES: ", totNos)

matrizDeAdj = []
matrizDeAdjDup = []

for i in range(totNos):
    matrizDeAdj.append( [0] * totNos)
    matrizDeAdjDup.append( [0] * totNos)

cont = -1

with open('data/edges.csv', 'r') as ficheiro:
    reader = csv.reader(ficheiro)
    for linha in reader:
        if cont == -1:
            cont += 1 
        else:
            matrizDeAdj[vetNos.index(linha[1])][vetNos.index(linha[2])] = round(float(linha[3]), 2)
            matrizDeAdjDup[vetNos.index(linha[1])][vetNos.index(linha[2])] = round(float(linha[3]), 2)
            matrizDeAdjDup[vetNos.index(linha[2])][vetNos.index(linha[1])] = round(float(linha[3]), 2)
            cont+=1

print(f"TOTAL DE ARCOS: {cont}")

arquivo = open("probExp.lp", 'w')
arquivo.writelines("Minimize\n")

aux = False
for i in range(totNos):
    for j in range(totNos):
        if matrizDeAdjDup[i][j] != 0:
            if not aux:
                aux = True
                dist = matrizDeAdjDup[i][j]
                arquivo.writelines(f"{dist} x{i}_{j}")
            else:
                dist = matrizDeAdjDup[i][j]
                arquivo.writelines(f" + {dist} x{i}_{j}")
                
arquivo.writelines("\n\nSubject to\n")

aux = False
imprime = False
for i in range(totNos):
    for j in range(totNos):
        if matrizDeAdjDup[i][j] != 0:
            if not aux:
                arquivo.writelines(f"(x{i}_{j}")
                aux = True
                imprime = True
            else:
                arquivo.writelines(f" + x{i}_{j}")
    if imprime:
        arquivo.writelines(") - ")
        aux = False
        for i2 in range(totNos):
            if matrizDeAdjDup[i2][i] != 0:
                if not aux:
                    arquivo.writelines(f"(x{i2}_{i}")
                    aux = True
                else:
                    arquivo.writelines(f" + x{i2}_{i}")
        
        
    
        arquivo.writelines(") = 0\n")
    aux = False
    imprime = False
    

arquivo.writelines("\nBounds\n")

for i in range(totNos):
    for j in range(totNos):
        if matrizDeAdj[i][j] != 0:
            arquivo.writelines(f"x{i}_{j} >= 1\n")

arquivo.writelines("\nEnd\n")

matrizDeAdjEuler = []
matrizhierh = []

for i in range(totNos):
    matrizDeAdjEuler.append( [0] * totNos)
    matrizhierh.append([])

arqData = input("Resolva o probExp.lp no solver e Insira o nome do arquivo com os resultados: ")
cont = 0
with open(arqData, 'r') as ficheiro:
    reader = csv.reader(ficheiro)
    for linha in reader:
        if cont == 0:
            cont += 1 
        else:
            matrizDeAdjEuler[int(linha[0][1])][int(linha[0][3])] = int(linha[1])
            for i in range (int(linha[1])):
                matrizhierh[int(linha[0][1])].append(int(linha[0][3]))

print("Percurso minimo:")
circ = hierh.printCircuit(matrizhierh)
circ.reverse()

for i in range(len(circ)):
        print(vetNos[circ[i]], end = "")
        if i<len(circ)-1:
            print(" -> ", end = "")


peso = 0
for i in range((len(circ)-1)):
    peso += matrizDeAdjDup[circ[i]][circ[i+1]]

print(f"\nDistância total do percurso:\n{round(peso, 2)}")        