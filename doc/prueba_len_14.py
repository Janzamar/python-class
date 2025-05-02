#Clasificación de Genes
#Dado un valor de expresión génica, clasifica el gen como sobreexpresado, expresión normal o baja expresión.
expresion = 5.2  # Cambia este valor

if expresion > 7 :
    print("Gen sobreexpresado")
elif expresion >= 5.2 and expresion <= 7 :
    print("Expresión normal")
else:
    print("Baja expresión")



# Verificación de Longitud de Secuencia
# Escribe un programa que verifique si una secuencia de ADN tiene más de 1000 bases.

secuencia = "ATGCGT..." # Coloca aquí una secuencia de ADN`

if len(secuencia) >= 6:
   print("Secuencia larga")
else:
  print("Secuencia corta")