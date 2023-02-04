import pyphen
dic = pyphen.Pyphen(lang='es')

def separar_silabas(palabra):
  return dic.inserted(palabra).split(" ")

frase = input('Escriba la frase: ')
palabras = frase.split()
silabas = [separar_silabas(palabra) for palabra in palabras]
print(silabas)