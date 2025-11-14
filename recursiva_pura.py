def recursiva_pura(pesos, valores, W, n=None):
    """
    Explora todas as combinações possíveis.

    Retorno:
    - int: O valor total maximizado ótimo.

    Complexidade:
    - O(2^n): Cada item tem duas escolhas (incluir/excluir),.
    - Ω(2^n): Pior caso.
    - Θ(2^n): Pior caso.
    """

    if n is None:
        n = len(pesos)

    if n == 0 or W == 0:
        return 0

    # Se o peso do item atual (n-1) é maior que a W este item não pode ser incluído.
    if pesos[n - 1] > W:
        return recursiva_pura(pesos, valores, W, n - 1)
    else:
        # 1. Inclui o item (n-1)
        incluir_item = valores[n - 1] + recursiva_pura(pesos, valores, W - pesos[n - 1], n - 1)
        # 2. Exclui o item (n-1)
        excluir_item = recursiva_pura(pesos, valores, W, n - 1)

        return max(incluir_item, excluir_item)

if __name__ == "__main__":
    pesos = [2, 3, 4, 1]
    valores = [10, 12, 20, 3]
    capacidade_max = 6

    print(f"Capacidade Máxima: {capacidade_max}")
    print(f"Pesos:   {pesos}")
    print(f"Valores: {valores}")
    print(f"Solução Ótima Esperada: 30") # A solução ótima é 30 (Pesos 2+4, Valores 10+20).
    print("-" * 40)

    # Recursiva Pura
    val_rec = recursiva_pura(pesos, valores, capacidade_max)
    print(f"1. Solução Recursiva Única: {val_rec}")
