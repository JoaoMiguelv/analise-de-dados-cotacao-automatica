# analise-de-dados
Análise de Dados utilizando Python e MySQL
Programa criado para a validação de informações do banco de dados interno da empresa, com as informações de disponibilidade e custo de produtos em seus respectivos fornecedores.

MOTIVO: Vários produtos Cross Docking estavam sendo vendidos com informações erradas, como o custo e disponibilidade. O que afetava diretamente a reputação da empresa nos Marketplaces ou efetuava vendas com margem de lucro mais baixa.

OBJETIVO: Manter todas as informações atualizadas para evitar conflito de dados.

RESULTADO: Anteriormente, apenas 75% das vendas em Cross Docking estavam sendo realizadas totalmente corretas. No primeiro mês de teste, com um script mais inferior a este, essa margem subiu de 75% para 90%.

O programa a seguir consiste em 3 passos:
1) Verificar no banco de dados as informações de custo e disponibilidade dos códigos cadastrados.
2) Ler planilha de cotação realizada diretamente no sistema do fornecedor, feita por Web Scraping (selenium) por conta da ausência de API.
3) Validar as informações das duas consultas citadas acima e alterar tudo o que for necessário direto pela API do sistema de integração usado pela empresa.
