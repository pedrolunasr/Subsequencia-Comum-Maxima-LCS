def lcs(a: str, b: str) -> str:
    """
    Retorna UMA Longest Common Subsequence (LCS) entre a e b.
    Complexidade: O(len(a)*len(b)) em tempo e memória.
    """
    n, m = len(a), len(b)

    # dp[i][j] = tamanho do LCS entre a[:i] e b[:j]
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Preenche a tabela
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstrói uma LCS voltando pela tabela
    i, j = n, m
    out = []
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            out.append(a[i - 1])
            i -= 1
            j -= 1
        else:
            # Preferência de caminho em empate: sobe (i-1,j).
            # Isso influencia qual LCS você obtém quando há mais de uma.
            if dp[i - 1][j] >= dp[i][j - 1]:
                i -= 1
            else:
                j -= 1

    return "".join(reversed(out))



a = "banana"
b = "benanani"
seq = lcs(a, b)
print("LCS:", seq)
print("Tamanho:", len(seq))
