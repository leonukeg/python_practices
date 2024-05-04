
lista = [12,16,20,20,12,30,25,23,24,20]
print(lista)
lista.sort() #reordena la lista de menor a mayor
print(f"\nla lista ordenada es: {lista}")
tamano = len(lista)
print(f"\nel largo de la lista es: {tamano}")

#media

media = sum(lista) / tamano
print(f"\nla media de la lista es: ´{media}")

#mediana

if tamano % 2 == 2: #si la lista es impar
    x1 = lista[tamano//2]
    x2 = lista[tamano//2 - 1]
    mediana = (x1 + x2) / 2
    print(f"\nla mediana es: {mediana}")
else: # si la lista es par
    mediana = lista[tamano // 2]
    print(f"\nla mediana es: {mediana}")

#moda

conter = {}
for dato in lista:
    if dato in conter:
        conter[dato] += 1
    else:
        conter[dato] = 1

moda = None
max_fre = 0
for dato, frecu in conter.ites():
    if frecu > max_fre:
        moda = dato
        max_fre = frecu


print(f"\nla moda es: {moda}")
