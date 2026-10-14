# ==========================================
# PARTE 3: SISTEMA DE RECOMENDAÇÃO (JACCARD)
# ==========================================

def calcular_afinidade(usuario1, interesses1, usuario2, interesses2):
    # Transforma as listas em conjuntos (sets)
    A = set(interesses1)
    B = set(interesses2)

    intersecao = A & B
    uniao = A | B

    # Evita divisão por zero caso os dois conjuntos sejam vazios
    if len(uniao) == 0:
        indice_jaccard = 0.0
    else:
        indice_jaccard = len(intersecao) / len(uniao)

    # Diferença B - A: o que B gosta e pode ser recomendado para A
    recomendacoes_para_A = B - A

    print(f"\n==========================================")
    print(f"Comparando {usuario1} e {usuario2}:")
    print(f"Interesses de {usuario1} (A): {A}")
    print(f"Interesses de {usuario2} (B): {B}")
    print(f"Em comum (A ∩ B): {intersecao} (Total: {len(intersecao)})")
    print(f"Todos juntos (A U B): {uniao} (Total: {len(uniao)})")
    print(f"Índice de Jaccard: {len(intersecao)}/{len(uniao)} = {indice_jaccard:.2f} ({indice_jaccard * 100:.0f}% de afinidade)")
    print(f"Recomendações para {usuario1} (B - A): {recomendacoes_para_A}")

# --- CENÁRIOS DE TESTE AUTOMÁTICOS ---
print("=== SISTEMA DE RECOMENDAÇÃO POR CONJUNTOS ===")

# Cenário 1: Afinidade parcial
calcular_afinidade(
    "Ana", ["Python", "Java", "SQL", "Git"],
    "Bruno", ["Python", "SQL", "HTML", "CSS"]
)

# Cenário 2: Sem afinidade (Conjuntos Disjuntos)
calcular_afinidade(
    "Carlos", ["Futebol", "Basquete"],
    "Diana", ["Xadrez", "Leitura"]
)

# Cenário 3: Afinidade Total (Conjuntos Iguais)
calcular_afinidade(
    "Eduardo", ["Rock", "MPB", "Jazz"],
    "Fernanda", ["Jazz", "Rock", "MPB"]
)