# ==========================================
# FUNÇÕES BÁSICAS FEITAS À MÃO (COM FOR E IF)
# ==========================================

def pertence(elemento, conjunto):
    """Verifica se um número está dentro da lista (x in A)"""
    for item in conjunto:
        if item == elemento:
            return True
    return False


def cardinalidade(conjunto):
    """Conta quantos elementos existem na lista (|A|)"""
    quantidade = 0
    for _ in conjunto:
        quantidade = quantidade + 1
    return quantidade


def uniao(a, b):
    """Junta os elementos de A e B sem repetir"""
    resultado = []
    # Copia os elementos de A
    for item in a:
        resultado.append(item)
    # Adiciona apenas os de B que ainda não estão no resultado
    for item in b:
        if not pertence(item, resultado):
            resultado.append(item)
    return resultado


def intersecao(a, b):
    """Pega apenas nos números que aparecem nos dois conjuntos"""
    resultado = []
    for item in a:
        if pertence(item, b):
            resultado.append(item)
    return resultado


def diferenca(a, b):
    """Pega nos números que estão em A mas NÃO estão em B"""
    resultado = []
    for item in a:
        if not pertence(item, b):
            resultado.append(item)
    return resultado


def diferenca_simetrica(a, b):
    """Elementos em A ou em B, mas não em ambos"""
    dif_ab = diferenca(a, b)
    dif_ba = diferenca(b, a)
    return uniao(dif_ab, dif_ba)


def subconjunto(a, b):
    """Verifica se todos os elementos de A estão dentro de B (A ⊆ B)"""
    for item in a:
        if not pertence(item, b):
            return False
    return True


def subconjunto_proprio(a, b):
    """A está contido em B, mas A não é igual a B (A ⊂ B)"""
    if subconjunto(a, b) and cardinalidade(a) < cardinalidade(b):
        return True
    return False


def complemento(a, universo):
    """Elementos do universo que não estão em A (U - A)"""
    return diferenca(universo, a)


# ==========================================
# LEITURA SIMPLES DE DADOS
# ==========================================

def ler_conjunto(nome):
    """Lê números digitados e guarda sem repetições"""
    texto = input(f"Digite os números de {nome} separados por espaço: ")
    itens = texto.split()
    
    lista_limpa = []
    for x in itens:
        numero = int(x)
        # Só adiciona se o número ainda não estiver na lista
        if not pertence(numero, lista_limpa):
            lista_limpa.append(numero)
            
    return lista_limpa


# ==========================================
# PROGRAMA PRINCIPAL E COMPARAÇÃO COM SET()
# ==========================================

if __name__ == "__main__":
    print("--- DEFINIÇÃO DOS CONJUNTOS ---")
    A = ler_conjunto("A")
    B = ler_conjunto("B")
    U = ler_conjunto("Universo U")

    print("\n--- CONJUNTOS INFORMADOS ---")
    print("A:", A, "| Tamanho:", cardinalidade(A))
    print("B:", B, "| Tamanho:", cardinalidade(B))
    print("U:", U, "| Tamanho:", cardinalidade(U))

    print("\n--- OPERAÇÕES (NOSSA IMPLEMENTAÇÃO MANUAL) ---")
    res_uniao = uniao(A, B)
    res_inter = intersecao(A, B)
    res_dif_ab = diferenca(A, B)
    res_dif_ba = diferenca(B, A)
    res_sim = diferenca_simetrica(A, B)
    res_comp = complemento(A, U)
    res_sub = subconjunto(A, B)
    res_sub_prop = subconjunto_proprio(A, B)

    print("União (A ∪ B):", res_uniao)
    print("Interseção (A ∩ B):", res_inter)
    print("Diferença (A - B):", res_dif_ab)
    print("Diferença (B - A):", res_dif_ba)
    print("Diferença Simétrica (A Δ B):", res_sim)
    print("Complementar de A em relação a U:", res_comp)
    print("A está contido em B (A ⊆ B)?", res_sub)
    print("A está contido propriamente em B (A ⊂ B)?", res_sub_prop)

    # Exigência da folha: validar comparando com a função nativa do Python
    print("\n--- VALIDAÇÃO COM O SET NATIVO DO PYTHON ---")
    set_a = set(A)
    set_b = set(B)
    
    print("União bate certo?", set(res_uniao) == (set_a | set_b))
    print("Interseção bate certo?", set(res_inter) == (set_a & set_b))
    print("Diferença A-B bate certo?", set(res_dif_ab) == (set_a - set_b))
    print("Subconjunto bate certo?", res_sub == set_a.issubset(set_b))