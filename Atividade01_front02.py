''' FOI UTIULIZADA A GEMINI!!
 PARA CORRECAO!!
 E COMENTARIOS DO CODIGO !

-Filipe Barbosa

'''



#CONTADORES E VARIAVEIS
maior_altura = 0.0
menor_altura = float('inf')  # Uso de infinito para garantir que a primeira altura seja a menor
soma_altura_feminino = 0.0
cont_f = 0
cont_m = 0

#LOOP : EM RANGE VOCE DEFINE A QUANTIDADE QUE QUER QUE ELE RODE O CODIGO
for i in range(5):
    nome = input(f"Pessoa {i + 1} - Digite seu nome: ")

    while True:
            altura = float(input(f"Oi, {nome}! Digite sua altura (em metros): "))
            if altura > 0:
                break
            else:
                print("Altura inválida. Digite um valor maior que zero.")

    while True:
        genero = input(f"Oi, {nome}! Informe seu gênero (M/F): ").upper()
        if genero in ['M', 'F']:
            break
        else:
            print("Gênero inválido. Digite 'M' ou 'F'.")

    #CONTAGEM DA ALTURA
    if altura > maior_altura:
        maior_altura = altura
    if altura < menor_altura:
        menor_altura = altura

    # CONTAGEM DO GENERO
    if genero == 'F':
        soma_altura_feminino += altura
        cont_f += 1
    elif genero == 'M':
        cont_m += 1

#RESULTADOS
print("===------RESULTADOS!------===")
print(f"A maior altura é: {maior_altura:.2f} m")
print(f"A menor altura é: {menor_altura:.2f} m")

if cont_f > 0:
    media_feminino = soma_altura_feminino / cont_f
    print(f"A média de altura das mulheres é: {media_feminino:.2f} m")
else:
    print("Nenhuma altura de mulher foi registrada.")

print(f"O número total de homens é: {cont_m}")