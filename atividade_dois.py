i = 0
continuar = 's'
prox_num = 0
while continuar == 's':
    num = float(input ("Digite um numero"))
    num += prox_num
    continuar = (input ("Deseja continuar? [s/n]")) 
    if num > prox_num:
        print (f"Esse numero: {num} e maior que {prox_num}")