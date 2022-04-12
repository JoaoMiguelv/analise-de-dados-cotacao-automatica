
from quotation_supplier.service_seg import quotation_seg

def busca_binaria(matriz_cotacao, martriz_produtos, token): # Busca binária (conceito de Estrutura de Dados) para melhor funcionamento do script
    cont = 0
    x = 1
    for i in range(len(matriz_cotacao)):
        val = matriz_cotacao[i][0]

        ini = 0
        fim = len(martriz_produtos)-1

        while ini <= fim:
            meio = (ini + fim) // 2 
            val_meio = martriz_produtos[meio][0][1]

            if val == val_meio:
                cont += 1
                x += 1
                search_found(val, val_meio, i, meio, matriz_cotacao, martriz_produtos, token) # Código encontrado na matriz
                break

            elif val > val_meio:
                ini = meio + 1
                continue

            else:
                fim = meio - 1
                continue
    
    #print(cont)
    

def search_found(val, val_meio, index_cotacao, index_prod, matriz_cotacao, martriz_produtos, token):
    # DEFININDO VARIÁVEIS PARA ALTERAR NA SEG PELA REQUISIÇÃO
    codigo = matriz_cotacao[index_cotacao][0]
    disponibilidade_forn= matriz_cotacao[index_cotacao][1]
    custo_for = matriz_cotacao[index_cotacao][2]

    cod_erp = martriz_produtos[index_prod][0][0] 
    disponibilidade_erp = martriz_produtos[index_prod][0][2]
    desc_fabricante = martriz_produtos[index_prod][0][3]
    estoque_atual = martriz_produtos[index_prod][0][4]
    custo_erp = martriz_produtos[index_prod][0][5]

    availability = 0
    supplier_id = 0
    id = cod_erp
    name = codigo

    # Tratando dados e definindo o que será alterado no sistema de integração

    if desc_fabricante == 'FORNECEDOR':
        supplier_id = 1

    elif desc_fabricante == 'FORNECEDOR X':
        supplier_id = 2


    if disponibilidade_forn == 'INDISPONÍVEL' and disponibilidade_erp == 'DISPONÍVEL':
        availability = 4
        quotation_seg(token, availability, id, name, supplier_id)
        
        status_log = 'DISPONÍVEL --> INDISPONÍVEL'
        cor = "00FF0000"

    ####################################################################################################################################
        
    if disponibilidade_forn == 'DISPONÍVEL': # NÃO DISPONIBILIZAR POIS TEM QUE VALIDAR O CUSTO

        diferenca_aceitavel = float(custo_erp)*0.10
        diferenca_custos = float(custo_for) - float(custo_erp)

        custo_forn_desconto = 'X'
        diferenca_custos_desconto = 'X'

        status_log = ''
        cor = ''

        if disponibilidade_erp == 'DISPONÍVEL':
            if diferenca_custos > diferenca_aceitavel:
                availability = 4
                status_log = 'DIFERENÇA > 10% NO CUSTO --> INDISPONÍVEL'
                cor = "00FF0000"

        elif disponibilidade_erp == 'INDISPONÍVEL':
        
            if diferenca_custos < diferenca_aceitavel:
                status_log = "INDISPONÍVEL --> DISPONÍVEL"
                cor ="000000FF"
                
                if diferenca_custos == 0:
                    cor ="00008000"

                availability = 1

        if desc_fabricante == 'FORNECEDOR X':
            custo_forn_desconto = float(custo_for)*0.8 # 20% de desconto
            diferenca_custos_desconto = float(custo_forn_desconto) - float(custo_erp)

            if diferenca_custos != 0:

                if diferenca_custos_desconto == 0 or (diferenca_custos_desconto > -0.10 and diferenca_custos_desconto < 0.10):
                    if disponibilidade_erp == 'INDISPONÍVEL':
                        availability = 1
                        status_log = "INDISPONÍVEL --> DISPONÍVEL (DESC. 20%)"
                        cor ="00008000"

                    elif disponibilidade_erp == 'DISPONÍVEL':
                        availability = 0
                        status_log = 'DISPONÍVEL E < 10% NO CUSTO --> MANTER (DESC. 20%)'
                        cor = "00000000"
        
        if availability != 0:
            quotation_seg(token, availability, id, name, supplier_id) # alteração direto pela api do sistema de integração usado pela empresa
 


    




