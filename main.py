cont = int(0)
soma = float(0)
positivos = int(0)
while cont < 6:
    numero = float(input())
    if (numero >= 0):
        positivos = positivos + 1
        soma = soma + numero
    cont = cont + 1
print("{} valores positivos".format(positivos))
media = float(soma / positivos)
print("%.1f"%(media))