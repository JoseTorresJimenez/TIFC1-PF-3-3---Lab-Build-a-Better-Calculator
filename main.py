#Recibe una lista de números y devuelve la suma de todos
def addmultiplenumbers(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

#Recibe una lista de números y devuelve el producto de todos
def multiplymultiplenumbers(numbers):
    result = 1
    for n in numbers:
        result *= n
    return result

#Devuelve True si el número es un entero
def isitaninteger(num):
    return num == int(num)

#Devuelve True si el número es entero y par
def isiteven(num):
    return isitaninteger(num) and num % 2 == 0

def main():
  #Muestra el menú y pide al usuario que elija una opción
  print("Calculadora")
  print("1) Sumar  2) Multiplicar  3) ¿Es entero y par?  4) ¿Es entero?")
  opcion = input("Elige una opción: ")

#Opcion 1 y 2: pide una lista de números y llama a la función correspondiente
  if opcion in ("1", "2"):
      texto = input("Escribe los números separados por espacios: ")
      # float(x) convierte cada texto en número
      numeros = [float(x) for x in texto.split()]
      if opcion == "1":
          #Se llama a la función addmultiplenumbers con la lista de números y se imprime el resultado
          print("Resultado:", addmultiplenumbers(numeros))
      else:
          #Se llama a la función multiplymultiplenumbers con la lista de números y se imprime el resultado
          print("Resultado:", multiplymultiplenumbers(numeros))
#Opcion 3 y 4: pide un número y llama a la función correspondiente
  elif opcion in ("3", "4"):
      num = float(input("Escribe un número: ")) #Se convierte el texto en número
      if opcion == "3":
          print(isiteven(num)) #Se llama a la función isiteven con el número y se imprime el resultado
      else:
          print(isitaninteger(num)) #Se llama a la función isitaninteger con el número y se imprime el resultado
  else:
      print("Opción no válida") #Si el usuario elige una opción no válida, se imprime un mensaje de error

if __name__=="__main__":
  main()