def knapsackPD(pesos, valores, W):
    """
    Resolve o Problema da Mochila 0/1 usando Programação Dinâmica (Abordagem Bottom-Up, iterativa).

    Retorno:
    - int: O valor total maximizado ótimo.

    Complexidade:
    - O(n * W): Dois loops aninhados, um até n e outro até W.
    - Ω(n * W): Sempre precisa preencher a tabela inteira.
    - Θ(n * W): Complexidade de tempo e espaço (para a tabela dp).
    """
    n = len(pesos)
    # Cria a tabela dp[i][w] que armazena o valor máximo usando os primeiros itens com essa capacidade.
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Constrói a tabela dp de forma iterativa (bottom-up)
    for i in range(1, n + 1):
        for w in range(1, W + 1):

            peso_item_atual = pesos[i - 1]
            valor_item_atual = valores[i - 1]

            # Verifica se o item atual (i-1) cabe na capacidade 'w'
            if peso_item_atual <= w:
                # Escolhe:
                # Incluir o item: seu valor + valor da mochila com capacidade restante (w - peso) e (i-1) itens.
                # Excluir o item: mesmo valor de (i-1) itens com capacidade 'w'.
                incluir = valor_item_atual + dp[i - 1][w - peso_item_atual]
                excluir = dp[i - 1][w]
                dp[i][w] = max(incluir, excluir)
            else:
                # O item não cabe, então o valor é o mesmo.
                dp[i][w] = dp[i - 1][w]

    # A solução final está na última célula da tabela
    return dp[n][W]


# --- Exemplo de Uso ---
if __name__ == "__main__":
    pesos = [2, 3, 4, 1]
    valores = [10, 12, 20, 3]
    capacidade_max = 6

    print(f"Capacidade Máxima: {capacidade_max}")
    print(f"Pesos:   {pesos}")
    print(f"Valores: {valores}")
    print(f"Solução Ótima Esperada: 30") # A solução ótima é 30 (Pesos 2+4, Valores 10+20).
    print("-" * 40)

    # PD (Bottom-Up)
    val_pd = knapsackPD(pesos, valores, capacidade_max)
    print(f"4. Programação Dinâmica (BU): {val_pd}")
