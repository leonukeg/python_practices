import random

def aleatorio(max,min):
    n= int(random.random() * (max-min+1) + min)
    return n

def genararletra():
    letras = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    numero = aleatorio(0,15)

    return letras[numero]

num = ""

for i in range(0,6):
    num = num + genararletra()

print("----------------------------------------")
print(f"busca el color en hexadecimal : #{num}")


