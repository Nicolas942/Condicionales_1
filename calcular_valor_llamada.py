cant_minutos = int(input("Digite la cantidad de minutos que duro la llamada ")) #input

if cant_minutos <= 3:
    print('el valor de la llamada son 300 pesos')

else:
    valor_llamada = 300+50*(cant_minutos-3)


print(f'el valor de la llamada son {valor_llamada} pesos')