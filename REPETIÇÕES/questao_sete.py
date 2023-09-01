num = int (input("Qual numero voce deseja tirar o fatorial?: "))
i = num
aux = num
while (i > 1):
    i = i - 1
    n = n * i

print ("Fatorial do {} numero e {}".format (aux,n))