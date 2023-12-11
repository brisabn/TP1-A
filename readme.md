# 📃Algoritmos de Busca
**ଘ(੭◌ˊ ᵕ ˋ)੭** ★ Este trabalho prático foi desenvolvido para a disciplina de Introdução a Inteligência Artificial, da Universidade Federal de Minas Gerais (UFMG). O objetivo era implementar seis algorimos de busca para encontrar a sequência de movimentos ideal para a solução de um 8-Puzzle. São esses: Breadth-First Search, Iterative Deepening Search, Uniform-Cost Search, A* Search, Greedy Best-First Search e Hill Climbing.

## ｡₊⊹⭒˚｡⋆Execução
Para a execução do programa, deve ser utilizado Python3.

Execução no Windows:
**```python TP1.py <algoritmo> <n1> <n2> <n3> <n4> <n5> <n6> <n7> <n8> <n9> [PRINT]```**

Cada parâmetro corresponde:
* **```<algoritmo>```**: Escolha o algoritmo de verificação. Deve ser uma das seguintes opções: 'B', 'I', 'U', 'A', 'G', 'H'.
* **```<n1> <n2> <n3> <n4> <n5> <n6> <n7> <n8> <n9>```**: Fornecer nove números como entrada inicial do 8-puzzle.
* **```[PRINT]```**: O parâmetro opcional "PRINT" permite a impressão dos passos intermediários da solução do problema.

Verifica se exatamente 9 números (peças) foram fornecidos e sejam diferentes uns dos outros, caso contrário, o programa exibirá uma mensagem de erro apropriada.

## ｡₊⊹⭒˚｡⋆Exemplo de uso
𖤐 Executa o Breadth-First Search e imprime os passos até a solução
```
python main.py B 1 5 2 4 0 3 7 8 6 PRINT
```
<p align="center">
  <img src="https://github.com/brisabn/TP1-IAI/assets/103007463/64fdab8b-40c9-49a4-abb3-6cc8f8180d8a)"http://some_place.com/image.png" />
</p>
