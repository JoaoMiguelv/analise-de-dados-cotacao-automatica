import firebirdsql

def bd_firebird():
    
    conn = firebirdsql.connect(user='USER', password='PASSWORD', database='PATH_DB', host='HOST_NAME', charset='UTF8') # Conectando ao banco de dados

    cursor = conn.cursor() # Aponta o banco de dados utilizado

    cursor.execute(
    f"SELECT CODPROD, CODFABRICANTE, DISPONIBILIDADE, DESCRFABRICANTE, ESTATUAL, CUSTOVAR FROM viewPRODUTO_VendasEV WHERE CODFABRICANTE != '' AND CUSTOVAR IS NOT NULL ORDER BY CODFABRICANTE"
    ) # Realizando a consulta

    martriz_produtos = [] # Definindo matriz

    for dados in cursor.fetchall(): #corre linha por linha na consulta realizada no cursor.execute
        dados_produto = []

        dados_produto.append(dados)
        martriz_produtos.append(dados_produto) # Inserindo todos os dados retornados pela consulta na matriz
    
    martriz_produtos.sort() # ordenando a matriz para realizar a busca binária

    conn.close # Fechando conexão

    return martriz_produtos
