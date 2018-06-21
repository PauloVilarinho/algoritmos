while True:
    try:
        palavras,linhas_por_pagina,caracteres_por_linha = [int(i) for i in input().split()]
        conto = input().split()
        paginas = 1
        linhas = 0
        tamanho_linha = 0
        for i in conto:
            if tamanho_linha != 0:
                if (tamanho_linha + len(i) + 1) <= caracteres_por_linha :
                    tamanho_linha += len(i) + 1
                else:
                    tamanho_linha = len(i)
                    if (linhas + 1) < linhas_por_pagina :
                        linhas += 1
                    else :
                        linhas = 0
                        paginas += 1
            else:
                tamanho_linha = len(i)
        print(paginas)
    except EOFError:
        break
