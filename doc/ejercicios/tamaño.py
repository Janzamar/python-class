with open("genes.gff") as file:
    for linea in file:
        columnas = linea.strip().split("\t")
        tamano =columnas[4]-columnas[3]+1
        print(linea)
