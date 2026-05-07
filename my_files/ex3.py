# Pipeline de Vendas de E-commerce
# Você recebeu um log (registro) do servidor de um e-commerce contendo as transações do dia. Os dados estão em uma lista de strings, onde cada string representa uma transação separada por vírgulas (formato CSV bruto). O formato de cada linha é:
# "ID_Transacao,ID_Usuario,Produto,Preco,Status"
# O Desafio
# Você precisa criar um pipeline de dados que processe esses logs brutos e descubra quem são os seus melhores clientes (aqueles que mais gastaram em compras concluídas).
# Regras do Pipeline:
# Extração (String para Tupla): Itere sobre a lista de logs. Divida cada string e converta os dados extraídos em uma tupla. Converta o preço de string para float.
# Filtragem (Condicional): Processe apenas as transações cujo status seja "COMPLETED". Ignore transações "FAILED" ou "PENDING".
# Agregação (Tupla para Dicionário): Crie um dicionário para somar o valor total gasto por cada usuário. A chave será o ID_Usuario e o valor será a soma dos preços de suas compras concluídas.
# Ordenação (Dicionário para Lista de Tuplas): Converta o dicionário final de volta para uma lista de tuplas no formato (ID_Usuario, Total_Gasto) e ordene essa lista do maior para o menor valor gasto.


# Código Base
# Copie o código abaixo e tente implementar a lógica.
# Python
# Dados brutos recebidos do servidor (Lista de Strings)
logs_brutos = [
    "T001,USER_99,Notebook,2500.00,COMPLETED",
    "T002,USER_15,Mouse,150.50,FAILED",
    "T003,USER_99,Teclado,300.00,COMPLETED",
    "T004,USER_42,Monitor,1200.00,COMPLETED",
    "T005,USER_15,Mouse,150.50,COMPLETED",
    "T006,USER_42,Cabo HDMI,45.00,PENDING",
    "T007,USER_99,Suporte,80.00,COMPLETED"
]


# ==========================================
# ESCREVA SEU PIPELINE AQUI

gasto_usuario = {}

for log in logs_brutos:
    # Extração

    dados = log.split(",")
    dados[3] = float(dados[3])
    tupla = tuple(dados)

    id_transacao, id_usuario, produto, preco, status = tupla
    
    print(f"\nLog analisado: {tupla}")

    # Filtragem
    if status == 'COMPLETED':
     
        # Agregação
        if id_usuario in gasto_usuario:
            print("Usuário já consta no BD, adicionando compra")
            gasto_usuario[id_usuario] += preco
        else: 
            print("Novo usuário no BD, criando entrada {usuário:preco}")
            gasto_usuario[id_usuario] = preco
    else: 
        print("Pulando entrada de log, transação não completa")


# Ordenação
top_usuarios = sorted(gasto_usuario.items(), key= lambda x:x[1], reverse=True)
print(f"\nTop Usuários:\n{top_usuarios}")



# ==========================================








# ==========================================
# A saída esperada é uma lista de tuplas ordenada:
