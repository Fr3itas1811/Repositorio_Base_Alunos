nota = float(input("digite a sua nota (notas validas de 0 ate 10: ") )

while nota < 0 or nota > 10:

    nota = float(input("invalido, di8gite novamente: ") )
    print(f"sua nota foi: {nota}")