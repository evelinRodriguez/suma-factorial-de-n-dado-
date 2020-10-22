#ingreado un nuero "n "entero positivo determinar factorial del mismo


a = int(input("escriba un numero:"))

def factorial (num):
  resultado = num

  for i in  range(num-1,1,-1):
    resultado = resultado *i 
  return resultado 

print(factorial (a))  

