# --- Variáveis para os resultados ---
maior_altura = 0.0
menor_altura = float('inf')  # Uso de infinito para garantir que a primeira altura seja a menor
soma_altura_feminino = 0.0
cont_f = 0
cont_m = 0

# --- Loop para coletar dados de 15 pessoas ---
for i in range(3):
    nome = input(f"Pessoa {i + 1} - Digite seu nome: ")

    # Validação simples para garantir que a altura seja um número
    while True:
            altura = float(input(f"Oi, {nome}! Digite sua altura (em metros): "))
            if altura > 0:
                break
            else:
                print("Altura inválida. Digite um valor maior que zero.")

    # Validação para o gênero
    while True:
        genero = input(f"Oi, {nome}! Informe seu gênero (M/F): ").upper()
        if genero in ['M', 'F']:
            break
        else:
            print("Gênero inválido. Digite 'M' ou 'F'.")

    # Atualiza a maior e menor altura
    if altura > maior_altura:
        maior_altura = altura
    if altura < menor_altura:
        menor_altura = altura

    # Contagem e soma por gênero
    if genero == 'F':
        soma_altura_feminino += altura
        cont_f += 1
    elif genero == 'M':
        cont_m += 1

# --- Apresentação dos resultados ---
print("=== RESULTADOS! ===")
print(f"A maior altura é: {maior_altura:.2f} m")
print(f"A menor altura é: {menor_altura:.2f} m")

if cont_f > 0:
    media_feminino = soma_altura_feminino / cont_f
    print(f"A média de altura das mulheres é: {media_feminino:.2f} m")
else:
    print("Nenhuma altura de mulher foi registrada.")

print(f"O número total de homens é: {cont_m}")