# ===============================================
# CÓDIGO PYTHON PARA SIMULAÇÃO DE PROCESSAMENTO DE DADOS
# ===============================================

def processar_transacoes(dados_vendas, taxa_imposto):
    """
    Processa uma lista de dicionários de vendas para calcular o total
    e formatar um relatório.
    """
    relatorio = []
    valor_total_bruto = 0.0
    
    print("--- Processando Transações de Venda ---")
    
    # 1. Itera sobre cada transação na lista
    for transacao in dados_vendas:
        produto = transacao["produto"]
        quantidade = transacao["quantidade"]
        preco_unitario = transacao["preco_unitario"]
        
        # 2. Calcula o subtotal e adiciona ao total bruto
        subtotal = quantidade * preco_unitario
        valor_total_bruto += subtotal
        
        # 3. Formata a linha para o relatório
        linha_relatorio = (
            f"Produto: {produto:<15} | "  # Alinhamento à esquerda com 15 espaços
            f"Qtde: {quantidade:<3} | "
            f"Subtotal: R$ {subtotal:8.2f}" # 8 espaços totais, 2 casas decimais
        )
        relatorio.append(linha_relatorio)

    # 4. Calcula impostos e valor final
    imposto_devido = valor_total_bruto * taxa_imposto
    valor_total_final = valor_total_bruto + imposto_devido

    # 5. Gera o relatório final
    print("\n" + "="*50)
    print("RELATÓRIO DE VENDAS DETALHADO:")
    print("="*50)
    for linha in relatorio:
        print(linha)
    
    print("-" * 50)
    print(f"VALOR BRUTO TOTAL:             R$ {valor_total_bruto:8.2f}")
    print(f"IMPOSTOS ({taxa_imposto*100:.0f}%):             R$ {imposto_devido:8.2f}")
    print(f"VALOR TOTAL FINAL:             R$ {valor_total_final:8.2f}")
    print("="*50)


# Bloco principal de execução
if __name__ == "__main__":
    
    # Dados de exemplo no formato de lista de dicionários
    vendas = [
        {"produto": "Mouse Pad", "quantidade": 2, "preco_unitario": 15.50},
        {"produto": "Teclado Mec.", "quantidade": 1, "preco_unitario": 349.90},
        {"produto": "Monitor 27'", "quantidade": 1, "preco_unitario": 1250.00},
        {"produto": "Webcam", "quantidade": 3, "preco_unitario": 75.25},
    ]

    # Taxa de imposto a ser aplicada (ex: 12%)
    imposto = 0.12

    # Chama a função de processamento
    processar_transacoes(vendas, imposto)