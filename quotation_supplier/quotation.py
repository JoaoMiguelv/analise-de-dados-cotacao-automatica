import pandas as pd

def get_forn(): # Leitura da cotação realizada no fornecedor por Web Scraping
    matriz_cotacao = []

    cotacao = pd.read_excel(r"C:\Cotar Automatico\Fornecedor\Cotação forn.xls")
    for i, codigo in enumerate (cotacao.loc[:, 'COD.FABRICANTE']):
        disp = cotacao.loc[i,'DISPONIBILIDADE']
        try:
            custo_forn = cotacao.loc[i , 'VALOR'].replace(',','.')
        
        except:
            custo_forn = cotacao.loc[i , 'VALOR']

        if disp == 'COMPRAR' or disp =='INDISPONÍVEL':
            disp = 'DISPONÍVEL'
        elif disp == 'SEM ESTOQUE':
            disp = 'INDISPONÍVEL'
        else:
            disp = 'INDISPONÍVEL'

        matriz_codCot = []
        matriz_codCot.append(codigo)
        matriz_codCot.append(disp)
        matriz_codCot.append(custo_forn)


        matriz_cotacao.append(matriz_codCot) # ordenando a matriz para realizar a busca binária
    
    matriz_cotacao.sort()
    return matriz_cotacao

