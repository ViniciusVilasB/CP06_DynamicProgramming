# CP 05: DYNAMIC PROGRAMMING

Projeto desenvolvido para o Checkpoint 5 da disciplina de Dynamic Programming do curso de Engenharia de Software.

---

## Integrantes

| Nome Completo              | RM       |
|----------------------------|----------|
| `Erik Yuuta Goto`          | `558076` |
| `Guilherme Vieira Augusto` | `557264` |
| `Vinicius Vilas Boas`      | `557843` |

---

## Descrição do Projeto

O cenário é simples: dado um conjunto de itens, cada um com um peso e um valor específicos, devemos determinar quais itens incluir em uma mochila de capacidade limitada para que o valor total dos itens na mochila seja maximizado.

O nome "0/1" deriva da restrição principal: para cada item, temos apenas duas opções — ou o pegamos (1) ou o deixamos (0). Não é permitido pegar frações de um item ou múltiplas cópias do mesmo.

---

## Solução Implementada

Para resolver o problema, foram implementadas duas quatro distintas, conforme solicitado:

### Função 1: Estratégia Gulosa (Iterativa)

* **Conceito:** A abordagem gulosa tenta encontrar a solução ótima fazendo a escolha localmente ótima em cada etapa.

* **Demonstração (Caso de Teste de Falha):**
    Vamos usar um conjunto de dados diferente do exemplo para provar que a abordagem gulosa falha.

    * **Capacidade (W):** 50
    * **Itens:**
        * Item A: peso=10, valor=60 (Razão: 6.0)
        * Item B: peso=20, valor=100 (Razão: 5.0)
        * Item C: peso=30, valor=120 (Razão: 4.0)

    1.  **Abordagem Gulosa (por razão):**
        * Pega o Item A (Razão 6.0). Valor: 60. Capacidade restante: 40.
        * Pega o Item B (Razão 5.0). Valor: 60 + 100 = 160. Capacidade restante: 20.
        * Não pode pegar o Item C (peso 30 > capacidade 20).
        * **Resultado Guloso: 160**

    2.  **Solução Ótima (PD):**
        * Pega o Item B. Valor: 100. Capacidade restante: 30.
        * Pega o Item C. Valor: 100 + 120 = 220. Capacidade restante: 0.
        * **Resultado Ótimo: 220**

    Como 220 > 160, a estratégia gulosa falhou em encontrar a solução ótima.

* **Complexidade:** **Θ(n log n)**, pois a etapa dominante é a ordenação dos itens pela sua razão valor/peso.

### Função 2: Recursiva Pura (Ingênua)

* **Conceito:** Esta é a tradução direta da definição recursiva do problema. Para cada item, a função explora duas possibilidades (dois ramos na árvore de recursão):
    1.  O item **é incluído** (se couber).
    2.  O item **é excluído**.
    A função então retorna o máximo entre essas duas escolhas.

* **Análise de Desempenho:**
  Esta abordagem é extremamente ineficiente devido à recomputação massiva de subproblemas sobrepostos.
* **Complexidade:** **O(2^n)**. Para cada um dos `n` itens, existem duas escolhas, levando a um tempo de execução exponencial.

### Função 3: Recursiva com Memoização (Top-Down)

* **Conceito:** Esta é uma versão otimizada da recursão pura. Ela usa um mecanismo de cache (como um array 2D ou dicionário) para armazenar os resultados dos subproblemas já resolvidos.

* **Melhoria na Eficiência:** A memoização "poda" efetivamente a árvore de recursão. Qualquer ramo que leve a um subproblema já calculado é interrompido imediatamente.

* **Complexidade:** **Θ(n * W)**. O número de subproblemas únicos é `n * W` (cada combinação de `n` itens restantes e capacidade `W`). Cada subproblema é resolvido apenas uma vez. O espaço também é `O(n * W)` para armazenar o cache.

### Função 4: Programação Dinâmica (Bottom-Up)

* **Conceito:** Esta é a abordagem iterativa da PD, conhecida como **Bottom-Up**. Em vez de começar do topo (problema principal) e usar recursão, ela começa de baixo (o problema mais simples) e constrói as soluções iterativamente.

* **Fluxo do Algoritmo:** A tabela é preenchida iterativamente, começando de `dp[0][0] = 0`. Para preencher `dp[i][w]`, o algoritmo olha para o item `i` e decide:
    1.  Se o item `i` **não for incluído**, o valor é `dp[i-1][w]`.
    2.  Se o item `i` **for incluído** (e couber), o valor é `valor[i] + dp[i-1][w - peso[i]]`.
    O algoritmo armazena o `max` dessas duas opções em `dp[i][w]`. A resposta final é o valor encontrado em `dp[n][W]`.

* **Vantagem sobre Memoização:** Ela evita a sobrecarga (overhead) de chamadas de função recursivas e os limites de profundidade da pilha de recursão do sistema.

* **Complexidade:** **Θ(n * W)**. O algoritmo consiste em dois loops aninhados que preenchem uma tabela de tamanho `(n+1) * (W+1)`. O espaço também é `O(n * W)`.
---

## 4. Conclusão

### Resumo Comparativo

| Abordagem | Tipo | Garante Ótimo? | Complexidade de Tempo |
| :--- | :--- | :---: | :--- |
| **Gulosa (Iterativa)** | Heurística | **Não** | Θ(n log n) |
| **Recursiva Pura** | Força Bruta | Sim | O(2^n) |
| **Memoização (Top-Down)** | Prog. Dinâmica | Sim | Θ(n * W) |
| **PD (Bottom-Up)** | Prog. Dinâmica | Sim | Θ(n * W) |

### Escolha Ótima

Os algoritmos mais eficientes e robustos para resolver o Problema da Mochila 0/1 são as duas abordagens de Programação Dinâmica: **Recursiva com Memoização (Top-Down)** e **PD Iterativa (Bottom-Up)**.

Ambos têm a mesma complexidade de tempo, **Θ(n * W)**, que é vastamente superior à complexidade exponencial da recursão pura.
