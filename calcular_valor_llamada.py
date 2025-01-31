cant_minutos = int(input("Digite la cantidad de minutos que duro la llamada ")) #input

if cant_minutos <= 3:
    print('el valor de la llama son 300 pesos')

else:
    valor_llama = 300+50*(cant_minutos-3)


print(f'el valor de la llama son {valor_llama} pesos')