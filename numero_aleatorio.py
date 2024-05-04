#numero de adivinanza version 2.0

import random

def aleatorio(max,min):
  #n= int(random.random()* (max-min+1)+min) esta es mi version de numero aleatorio entero
  n = random.randrange(1,10)
  return n

x = aleatorio(1,10)
target = int(input("\ningrese un numero entre 1 y 10 -> "))

while target != x:
  
  if target > x:
      
    print("\nDispara mas bajo ")
    target = int(input("\nintentalo de nuevo -> "))
    
  elif target < x:
    print(" \nDispara mas arriba")
    target =int( input("\nintentalo de nuevo -> "))
    
  else:
    break

print(f"\ntriunfaste el numero es {x}\n")
