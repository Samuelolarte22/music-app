import pyphen
dic = pyphen.Pyphen(lang='es')

def separar_silabas(palabra):
  return dic.inserted(palabra).split(" ")

frase = input('Ingrese la frase: ')
palabras = frase.split()
silabas = [separar_silabas(palabra) for palabra in palabras]

silabas_separadas = []
for silaba_lista in silabas:
    for silaba in silaba_lista:
        silabas_separadas.append(silaba)

print(silabas_separadas)