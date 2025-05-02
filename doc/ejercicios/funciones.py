secuencia = "GTTCGACTA"

for i, base in enumerate(secuencia):
    print(f"Posicion {i} : {base}")

# funcion zip
bases = "ATGC"
complementos = "TACG"

for base, complemento in zip(bases, complementos):
    print (f"{base}--> {complemento}")