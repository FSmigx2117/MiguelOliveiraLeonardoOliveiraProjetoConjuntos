# ==========================================
# PARTE 2: CLASSIFICADOR DE NÚMEROS (CORRIGIDO)
# ==========================================
import math

def mostrar_resultado(tipo, pertence, nao_pertence, obs="", geratriz=None):
    print(f"Tipo: {tipo}")
    if geratriz:
        print(f"Fração geratriz: {geratriz}")
    print(f"Pertence a: {pertence}")
    print(f"Não pertence a: {nao_pertence}")
    if obs:
        print(f"Justificativa: {obs}")

def classificar_numero(entrada):
    # Padroniza vírgula para ponto e remove espaços extras
    texto = entrada.strip().replace(",", ".")

    # 1. Caso Raiz (VEM PRIMEIRO): aceita √9, √2, raiz(9) ou raiz(2)
    if texto.startswith("√") or texto.lower().startswith("raiz("):
        if texto.startswith("√"):
            valor = float(texto[1:])
        else:
            valor = float(texto[5:-1])
            
        raiz = math.sqrt(valor)
        if raiz.is_integer():
            mostrar_resultado("raiz exata", "N, Z, Q, R", "I", f"A raiz é exata e vale {int(raiz)}.")
        else:
            mostrar_resultado("raiz não exata", "I, R", "N, Z, Q", f"Raiz não exata ({raiz:.4f}...), portanto irracional.")

    # 2. Caso Dízima Periódica com parênteses: ex: 0,(3) ou 1,2(5)
    elif "." in texto and "(" in texto and texto.endswith(")"):
        negativo = texto.startswith("-")
        limpo = texto.lstrip("-")
        parte_int, resto = limpo.split(".")
        nao_periodica, periodo = resto[:-1].split("(")

        tudo = int(parte_int + nao_periodica + periodo)
        sem_periodo = int(parte_int + nao_periodica)
        numerador = tudo - sem_periodo
        denominador = int("9" * len(periodo) + "0" * len(nao_periodica))

        if negativo:
            numerador = -numerador

        mdc = math.gcd(numerador, denominador)
        num_simp = numerador // mdc
        den_simp = denominador // mdc

        if nao_periodica == "":
            info_tipo = f"dízima periódica simples (período: {periodo})"
        else:
            info_tipo = f"dízima periódica composta (parte não periódica: {nao_periodica}; período: {periodo})"

        # Caso especial como 0,(9) onde 9/9 = 1
        if den_simp == 1:
            geratriz_str = f"{numerador}/{denominador} = {num_simp}"
            if num_simp >= 0:
                mostrar_resultado(info_tipo, "N, Z, Q, R", "I", f"Caso curioso: a geratriz é {geratriz_str}.", geratriz_str)
            else:
                mostrar_resultado(info_tipo, "Z, Q, R", "N, I", f"A geratriz resulta no inteiro negativo {num_simp}.", geratriz_str)
        else:
            geratriz_str = f"{num_simp}/{den_simp}"
            mostrar_resultado(info_tipo, "Q, R", "N, Z, I", "Dízima periódica possui fração geratriz, logo é racional.", geratriz_str)

    # 3. Caso Dízima Periódica com reticências: ex: 0.333...
    elif texto.endswith("..."):
        limpo = texto.replace("...", "")
        partes = limpo.split(".")
        parte_inteira = int(partes[0])
        decimais = partes[1]

        periodo = decimais[0]
        for tam in range(1, len(decimais) // 2 + 1):
            trecho = decimais[:tam]
            repeticoes = len(decimais) // tam
            if trecho * repeticoes == decimais[:tam * repeticoes]:
                periodo = trecho
                break

        denominador = int("9" * len(periodo))
        numerador = abs(parte_inteira) * denominador + int(periodo)
        if texto.startswith("-"):
            numerador = -numerador

        mdc = math.gcd(numerador, denominador)
        geratriz_str = f"{numerador // mdc}/{denominador // mdc}"
        mostrar_resultado(f"dízima periódica (período: {periodo})", "Q, R", "N, Z, I", "Dízima periódica transformada em fração.", geratriz_str)

    # 4. Caso Fração: ex: 3/4, -5/2, 6/3
    elif "/" in texto:
        num, den = texto.split("/")
        num, den = int(num), int(den)
        if den == 0:
            print("Erro: Divisão por zero não existe!")
        elif num % den == 0:
            res = num // den
            if res >= 0:
                mostrar_resultado("fração aparente (inteiro natural)", "N, Z, Q, R", "I", f"A fração simplifica para {res}.")
            else:
                mostrar_resultado("fração aparente (inteiro negativo)", "Z, Q, R", "N, I", f"A fração simplifica para {res}.")
        else:
            decimal_eq = num / den
            mostrar_resultado("fração própria/imprópria", "Q, R", "N, Z, I", f"Fração equivalente ao decimal {decimal_eq}.")

    # 5. Caso Decimal Exato: ex: 0.75 ou 2,5
    elif "." in texto:
        valor = float(texto)
        if valor.is_integer():
            if valor >= 0:
                mostrar_resultado("decimal exato (inteiro)", "N, Z, Q, R", "I", f"Equivale ao natural {int(valor)}.")
            else:
                mostrar_resultado("decimal exato (inteiro negativo)", "Z, Q, R", "N, I", f"Equivale ao inteiro {int(valor)}.")
        else:
            mostrar_resultado("decimal exato", "Q, R", "N, Z, I", "Número decimal finito, pode ser escrito como fração.")

    # 6. Caso Inteiro: ex: 7, -3, 0
    else:
        try:
            valor = int(texto)
            if valor >= 0:
                mostrar_resultado("número natural", "N, Z, Q, R", "I", "Número natural (considerando 0 pertencente a N).")
            else:
                mostrar_resultado("inteiro negativo", "Z, Q, R", "N, I", "Inteiro negativo, não é natural.")
        except ValueError:
            print("Formato inválido! Use exemplos como: 7, -3, 3/4, 0,(3), 1,2(5), √2 ou raiz(2).")


# --- PROGRAMA PRINCIPAL ---
print("=== CLASSIFICADOR DE NÚMEROS - PARTE 2 ===")
print("Exemplos: 7 | -3 | 0 | 3/4 | -5/2 | 6/3 | 0,(3) | 2,(7) | 1,2(5) | 0,(9) | √9 | raiz(2)")

while True:
    numero = input("\nDigite um número para classificar (ou 'sair' para encerrar): ")
    if numero.lower() == "sair":
        print("A encerrar o programa...")
        break
    classificar_numero(numero)