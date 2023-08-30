i = 0
somas_das_notas = 0
continuar = 's'
while continuar == 's':
    nota = float(input("Digite a nota: "))
    somas_das_notas += nota
    continuar = (input("Deseja continuar [s/n]"))
    i +=1
media = somas_das_notas / i
print(media)

    