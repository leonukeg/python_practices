import random

def aleatorio(max,min):

  n= int(random.random()* (max-min+1)+min)
  return n

x =int(input("ingrese su apuesta (del 1 al 10)"))

print(f"su apuesta fue de: {x}\n")



while x != 0:

    a = aleatorio(0,7)
    b = aleatorio(0,7)
    c = aleatorio(0,7)

    print(f"{a},{b},{c}")

    if a == b and b == c:

        print("haz GANADO :)")
        x += 1
        print(f"ahora tiene {x}\n")

    else:

        print("intentalo de nuevo")
        x -= 1
        print(f"ahora tiene {x}\n")
