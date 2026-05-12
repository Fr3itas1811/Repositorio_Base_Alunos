from unittest import result


numero =  int(input("digite o numero para tabuada: ") )
inicio = int(input("digite o numero que a tabuada vai começar: ") )
repetiçao = int(input("digite o numero de repetiçoes: ") )

for i in range(inicio,repetiçao + 1):
    print(i)    
resultado = (numero * i) 
print(f"{numero} x {i} = {resultado} ")
