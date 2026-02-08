def extrair_lcs(s1, s2):
    lcs = []
    i = len(s1)
    j = len(s2)

    matriz = [[0 for _ in range(i + 1)] for _ in range(j + 1)]
    # Enquanto não chegarmos no topo ou na borda esquerda da matriz
    while i > 0 and j > 0:
        # Se os caracteres são iguais, eles fazem parte da subsequência!
        if s1[i-1] == s2[j-1]:
            lcs.append(s1[i-1])
            i -= 1
            j -= 1
        # Caso contrário, vamos para a direção do maior valor vizinho
        elif matriz[i-1][j] > matriz[i][j-1]:
            i -= 1
        else:
            j -= 1

    # Como começamos do fim, precisamos inverter a lista
    return "".join(reversed(lcs))


extrair_lcs("Pedro", "Pedra")