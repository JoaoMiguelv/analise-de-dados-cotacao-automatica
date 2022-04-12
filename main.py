from quotation_supplier.quotation import get_forn
from database.query_bd import bd_firebird
from search_data.disp_validation import busca_binaria
from quotation_supplier.service_seg import login


def main():
    global forn
    martriz_produtos = bd_firebird() # Consulta no banco de dados
    token = login()

    print('\nValidando Cotação...')
    try:
        matriz_cotacao = get_forn()
        busca_binaria(matriz_cotacao, martriz_produtos, token)
        print('Sucesso!')
    except:
        print('Erro ao ler Cotação.xls')



if __name__ == "__main__":
    main()
