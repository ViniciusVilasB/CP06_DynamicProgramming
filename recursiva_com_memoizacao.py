def recursiva_com_memoizacao(pesos, valores, W, n=None, memo=None):
    """
    Resolve o Problema da Mochila 0/1 com memoização em uma única função.

    Retorno:
    - int: O valor total maximizado ótimo.

    Complexidade:
    - O(n * W): Número de subproblemas únicos é n * W..
    - Ω(n * W): No pior caso, todos os estados da tabela são preenchidos.
    - Θ(n * W): Complexidade de tempo e espaço (para o memo).
    """

    if n is None:
        n = len(pesos)

    # Inicializa a tabela de memoização.
    if memo is None:
        # Precisa da W máxima original e do número máximo de itens.
        capacidade_original = W
        total_itens = n
        memo = [[-1 for _ in range(capacidade_original + 1)] for _ in range(total_itens + 1)]

    # Caso base
    if n == 0 or W == 0:
        return 0

    # Verifica se o subproblema já foi resolvido
    if memo[n][W] != -1:
        return memo[n][W]

    # Lógica recursiva (se não estava no memo)
    if pesos[n - 1] > W:
        # Item não cabe. Chama a para o próximo item (n-1).
        resultado = recursiva_com_memoizacao(pesos, valores, W, n - 1, memo)
    else:
        # Incluir o item (n-1)
        incluir_item = valores[n - 1] + recursiva_com_memoizacao(pesos, valores, W - pesos[n - 1], n - 1, memo)
        # Excluir o item (n-1)
        excluir_item = recursiva_com_memoizacao(pesos, valores, W, n - 1, memo)

        resultado = max(incluir_item, excluir_item)

    # Armazena o resultado no memo antes de retornar
    memo[n][W] = resultado
    return resultado

if __name__ == "__main__":
    pesos = [2, 3, 4, 1]
    valores = [10, 12, 20, 3]
    capacidade_max = 6

    print(f"Capacidade Máxima: {capacidade_max}")
    print(f"Pesos:   {pesos}")
    print(f"Valores: {valores}")
    print(f"Solução Ótima Esperada: 30") # A solução ótima é 30 (Pesos 2+4, Valores 10+20).
    print("-" * 40)

    # Memoização (Top-Down)
    val_memo = recursiva_com_memoizacao(pesos, valores, capacidade_max)
    print(f"Função Única com Memoização: {val_memo}")
