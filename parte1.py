# ==========================================
# PARTE 1: TEORIA DOS CONJUNTOS
# ==========================================

def ler_conjunto(nome):
    entrada = input(f"Digite os elementos de {nome} (separados por espaço ou vírgula): ")
    # Troca vírgulas por espaço para aceitar "1, 2, 3" ou "1 2 3"
    itens = entrada.replace(",", " ").split()
    conjunto = []
    for item in itens:
        if item not in conjunto:
            conjunto.append(item)
    return conjunto

# --- FUNÇÕES MANUAIS (USANDO LAÇOS E CONDICIONAIS) ---

def uniao(a, b):
    resultado = []
    for x in a:
        resultado.append(x)
    for x in b:
        if x not in resultado:
            resultado.append(x)
    return (resultado)

def intersecao(a, b):
    resultado = []
    for x in a:
        if x in b:
            resultado.append(x)
    return (resultado)

def diferenca(a, b):
    resultado = []
    for x in a:
        if x not in b:
            resultado.append(x)
    return (resultado)

def dif_simetrica(a, b):
    parte1 = diferenca(a, b)
    parte2 = diferenca(b, a)
    return uniao(parte1, parte2)

def subconjunto(a, b):
    for x in a:
        if x not in b:
            return False
    return True

# --- PROGRAMA PRINCIPAL ---
print("=== LABORATÓRIO DE CONJUNTOS - PARTE 1 ===")
U = ler_conjunto("Universo (U)")
A = ler_conjunto("A")
B = ler_conjunto("B")

while True:
    print("\n--- MENU DE OPERAÇÕES ---")
    print("1. União, Interseção, Diferenças e Diferença Simétrica")
    print("2. Pertinência (x in A) e Inclusão (A contido em B)")
    print("3. Cardinalidade e Complemento de A em U")
    print("4. Trocar conjuntos A, B e U")
    print("0. Sair")
    
    opcao = input("Escolha uma opção: ")
    set_U, set_A, set_B = set(U), set(A), set(B)

    if opcao == "1":
        print(f"\nA = {(A)} | |A| = {len(A)}")
        print(f"B = {(B)} | |B| = {len(B)}")
        print(f"União (A U B): {uniao(A, B)}")
        print(f"Interseção (A ∩ B): {intersecao(A, B)}")
        print(f"Diferença (A - B): {diferenca(A, B)}")
        print(f"Diferença (B - A): {diferenca(B, A)}")
        print(f"Dif. Simétrica (A Δ B): {dif_simetrica(A, B)}")

    elif opcao == "2":
        x = input("Digite um elemento 'x' para testar se pertence a A: ").strip()
        pertence = False
        for item in A:
            if item == x:
                pertence = True

        contido_igual = subconjunto(A, B)
        contido_proprio = contido_igual and (len(A) < len(B))

        print(f"\n{x} pertence a A?  = {pertence}")
        print(f"A ⊆ B (subconjunto)? = {contido_igual}")
        print(f"A ⊂ B (próprio)?  = {contido_proprio}")

    elif opcao == "3":
        cont_A = 0
        for _ in A:
            cont_A += 1
        comp = diferenca(U, A)

        print(f"\nCardinalidade |A|: = {cont_A}")
        print(f"Complemento de A em U: = {comp}")

    elif opcao == "4":
        U = ler_conjunto("Universo (U)")
        A = ler_conjunto("A")
        B = ler_conjunto("B")

    elif opcao == "0":
        break