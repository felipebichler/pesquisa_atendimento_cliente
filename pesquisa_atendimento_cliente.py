# Pesquisa de atendimento ao cliente
# Autor: Felipe Bichler

# Retorno com respostas excelentes e ruins
excelente = 0
ruim = 0

# Definindo o total de entrevistados
total_entrevistados = 50

print("Pesquisa de Atendimento ao Cliente - Tudo Web")

# Estrutura de repetição para coletar os dados dos entrevistados
for i in range(1, total_entrevistados + 1):
    print(f"\nEntrevistado {i} de {total_entrevistados}")
    
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    
    # Validação e coleta da opinião
    print("Opinião sobre o atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")
    
    opiniao = int(input("Digite a sua opção (1, 2 ou 3): "))
    
    # Estrutura de decisão para contagem dos resultados
    if opiniao == 1:
        excelente += 1
    elif opiniao == 3:
        ruim += 1

# Exibição do Resultado Parcial da pesquisa
    print("\nResultado Parcial da Pesquisa:")
    print(f"Total de entrevistas realizadas até agora: {i}")
    print(f"-> EXCELENTE: {excelente}")
    print(f"-> RUIM: {ruim}")

# Exibição do resultado final da pesquisa
print("Resultado da pesquisa:")
print(f"a) Quantidade de respostas 'EXCELENTE': {excelente}")
print(f"b) Quantidade de respostas 'RUIM': {ruim}")