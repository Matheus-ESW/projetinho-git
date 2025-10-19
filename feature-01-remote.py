# ===============================================
# CÓDIGO PYTHON SIMPLES PARA TESTES
# ===============================================

def calcular_e_imprimir(numero_base, limite):
    """
    Esta função calcula o quadrado de um número e imprime o resultado
    se for menor que o limite.
    """
    print(f"--- Iniciando teste com o número base: {numero_base} ---")
    
    contador = 0
    
    # Loop de 0 até (limite - 1)
    for i in range(limite):
        resultado = numero_base ** i  # Calcula a potência: numero_base elevado a 'i'
        
        if resultado < 1000:
            print(f"Iteração {i}: {numero_base}^{i} = {resultado}")
            contador += 1
        else:
            # Para o loop se o resultado for muito grande
            print(f"Iteração {i}: Resultado ({resultado}) excedeu 1000. Parando o loop.")
            break
            
    print(f"\n--- Fim do teste. Total de {contador} resultados exibidos. ---")

# Bloco principal de execução
if __name__ == "__main__":
    # 1. Defina os valores para teste
    base = 5
    max_iteracoes = 8
    
    # 2. Chama a função para iniciar o teste
    calcular_e_imprimir(base, max_iteracoes)

    # 3. Adiciona uma linha de separação e uma mensagem final
    print("\n==============================================")
    print("Teste finalizado com sucesso!")
    print("==============================================")