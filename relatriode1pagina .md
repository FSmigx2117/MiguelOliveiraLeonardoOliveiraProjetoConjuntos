# Relatório Técnico: Laboratório de Conjuntos

**Curso:** Desenvolvimento de Software Multiplataforma — Fatec Osasco  
**Atividade:** Teoria dos Conjuntos e Conjuntos Numéricos  
**Integrantes:** Leonardo Samuel Oliveira / Miguel Pires de Oliveira  

---

## 1. Onde a Teoria dos Conjuntos apareceu no código?

A Teoria dos Conjuntos serviu como base lógica e estrutural em todas as etapas do projeto, traduzindo conceitos matemáticos abstratos em algoritmos práticos:

- **Na Parte 1 (Operações Fundamentais):** A teoria apareceu diretamente na garantia de unicidade dos elementos (um conjunto não possui elementos repetidos). Ao ler os dados do usuário em uma lista, aplicamos um filtro de pertinência (`not in`) para descartar duplicatas. Além disso, as definições formais de união ($x \in A \text{ ou } x \in B$), interseção ($x \in A \text{ e } x \in B$) e diferença ($x \in A \text{ e } x \notin B$) foram traduzidas literalmente em estruturas de repetição `for` combinadas com condicionais `if`. O conceito de conjunto universo ($U$) também foi essencial para calcular o conjunto complementar de $A$ ($\overline{A} = U - A$).
- **Na Parte 2 (Conjuntos Numéricos):** A teoria manifestou-se na relação de inclusão hierárquica entre os conjuntos numéricos ($\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$) e na disjunção entre Racionais ($\mathbb{Q}$) e Irracionais ($\mathbb{I}$). No código, quando um número é identificado como inteiro positivo (ex: $10$), a propriedade de subconjunto garante automaticamente que ele também pertence a $\mathbb{Z}$, $\mathbb{Q}$ e $\mathbb{R}$. Da mesma forma, ao verificar raízes não exatas (como $\sqrt{2}$), aplicamos a definição de números irracionais, classificando-os em $\mathbb{I}$ e $\mathbb{R}$, mas excluindo-os de $\mathbb{Q}$.
- **Na Parte 3 (Sistema de Recomendação):** A teoria dos conjuntos foi aplicada como ferramenta de análise de dados. Cada perfil de usuário foi modelado como um conjunto finito de interesses. Utilizamos a razão entre a cardinalidade da interseção e a cardinalidade da união — conhecida como **Índice de Jaccard**, $J(A,B) = \frac{|A \cap B|}{|A \cup B|}$ — para medir o grau de similaridade entre duas pessoas. Por fim, a operação de diferença ($B - A$) permitiu isolar elementos inéditos para gerar recomendações reais.

---

## 2. Qual operação foi mais difícil de implementar e por quê?

Ao longo do desenvolvimento das três partes, duas operações se destacaram pela complexidade lógica:

1. **Identificação de Dízimas Periódicas e Cálculo da Fração Geratriz (Parte 2):**  
   Esta foi a implementação mais desafiadora do projeto. Em Python, números de ponto flutuante (`float`) têm precisão limitada e não armazenam a informação de que uma sequência decimal se repete infinitamente. Por isso, foi necessário tratar a entrada como texto (`string`), remover as reticências (`...`) e criar um laço de repetição capaz de testar fatias (*slices*) da parte decimal para descobrir qual era o período exato da dízima (se tinha $1$, $2$ ou mais algarismos repetidos). Após isolar o período, precisamos aplicar a regra algébrica de montar o denominador com noves (`9`), somar com a parte inteira e utilizar o cálculo do Máximo Divisor Comum (`math.gcd`) para entregar uma fração geratriz simplificada e exata (como converter `0.333...` em `1/3`).

2. **Verificação Manual de Subconjunto e Subconjunto Próprio (Parte 1):**  
   Sem o uso dos operadores prontos do Python (`<=` e `<`), implementar a inclusão ($A \subseteq B$ e $A \subset B$) exigiu cuidado com a lógica booleana. Um erro comum de iniciante é retornar `True` assim que encontra o primeiro elemento de $A$ dentro de $B$. Para corrigir isso, foi preciso estruturar a função para procurar um contraexemplo: percorrer todos os elementos de $A$ e, caso algum elemento não pertença a $B$, interromper o laço retornando `False`. Somente após o término completo do laço — inclusive garantindo que o conjunto vazio $\emptyset$ retorne `True` para qualquer conjunto $B$ — é que a função confirma a relação de inclusão.