def estrategia_gulosa(pesos, valores, W):
    """
    Esta abordagem não garante a solução ótima para o problema 0/1.

    Retorno:
    - int: O valor total maximizado (segundo a heurística gulosa).

    Complexidade:
    - O(n log n): Dominado pela ordenação dos itens.
    - Ω(n log n): A ordenação é sempre necessária.
    - Θ(n log n): Complexidade média e de pior caso.
    """

    n = len(pesos)
    # Cria uma lista de tuplas (razao, peso, valor)
    items = []
    for i in range(n):
        # Evita divisão por zero se o peso for 0
        if pesos[i] != 0:
            razao = valores[i] / pesos[i]
        else :
            float('inf')
        items.append((razao, pesos[i], valores[i]))

    # Ordena os itens pela razão em ordem decrescente
    items.sort(key=lambda item: item[0], reverse=True)

    total_valor = 0
    capacidade_restante = W

    # Itera pelos itens ordenados e os adiciona se couberem
    for razao, peso, valor in items:
        if peso <= capacidade_restante:
            total_valor += valor
            capacidade_restante -= peso

    return total_valor

if __name__ == "__main__":
    pesos = [2, 3, 4, 1]
    valores = [10, 12, 20, 3]
    capacidade_max = 6

    print(f"Capacidade Máxima: {capacidade_max}")
    print(f"Pesos:   {pesos}")
    print(f"Valores: {valores}")
    print(f"Solução Ótima Esperada: 30") # Saída esperada (ótima): 30 (Itens A + C)
    print("-" * 40)

    # Gulosa
    # Nota: Para este conjunto de dados, a gulosa acidentalmente encontra a solução ótima (A: r=5, C: r=5, B: r=4, D: r=3).
    # Ela pegaria A (cap=4) e C (cap=0) -> Valor 30.
    valor = estrategia_gulosa(pesos, valores, capacidade_max)
    print(f"1. Estratégia Gulosa (Iterativa): {valor}")

