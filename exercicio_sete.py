x =  int (input("Digite a posicao X: "))
y = int (input ("Digite a posicao Y: "))

if x > 0 and y > 0:
    print (f"O ponto {x} e ponto {y} esta localizado no primerio quadrante") 
    

elif x < 0 and y > 0:
    print (f"O ponto {x} e ponto {y} esta localizado no segundo quadrante") 

elif x < 0 and y < 0:
    print (f"O ponto {x} e ponto {y} esta localizado no terceiro quadrante") 

elif x > 0 and y < 0:
    print (f"O ponto {x} e ponto {y} esta localizado no quarto quadrante") 

    