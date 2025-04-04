secuencia = tuple("ATGCGTAGC")


#forma 1
# print(secuencia.count("A"),secuencia.count("T"), secuencia.count("G"), secuencia.count("C"))

# forma 2. comprensión de listas

#bases = list("ATCG")
# freq = [(bases, secuencia.count(bases)) for base in bases]

#forma 3. ciclos
for base in "ATCG":
    print(f"{secuencia.count(base)} bases {base}")