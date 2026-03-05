# Estruturas de dados lineares
# Tupla = lista imutável, utiliza ()

nums = (5,6,25,456,32.4,-8,5)
# nums = 5,6,25,456,32.4,-8,5 # Sem parênteses

#nums[4] = 42           # Erro, não é possível alterar

# print(nums[3])          # Busca pelo índice
# print(nums[-4])         # Busca pelo índice negativo (tras pra frente)
# print(len(nums))        # Quantidade de elementos
# print(nums.count(5))    # Quantidade de um elemento específico
# print(nums.index(25))   # Indice de um elemento
# print(sum(nums))        # Soma dos elementos numéricos

# for n in nums:
#     print(n)

# sub_tupla = nums[0:2]
# nums_invertido = nums[::-1]
# print(sub_tupla)
# print(nums_invertido)
# print(nums)

# cliente_1 = ("Marcos", 54, "SP", "4623897", False)
# print("Nome:",cliente_1[0])
# print("Idade:",cliente_1[1])
# print("Estado:",cliente_1[2])
# print("RG:",cliente_1[3])
# print("Ativo:",cliente_1[4])

# cliente_2 = ("Yasmin", 34, "DF", "3258746", True)
# cliente_3 = ("Luan", 27, "RJ", "1248965", True)

# cadastro = []
# cadastro.append(cliente_1)
# cadastro.append(cliente_2)
# cadastro.append(cliente_3)
# print(cadastro)

# Exemplo de função com mais de um retorno em forma de tupla
def calcular_geometria(lado):
    area = lado ** 2
    perimetro = lado * 4
    return area, perimetro #Tupla (area,perimetro)

resultado_area, resultado_perimetro = calcular_geometria(5)
print(resultado_area)
print(resultado_perimetro)
