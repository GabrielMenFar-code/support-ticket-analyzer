import pandas as pd

def analyze_tickets():
    # Simulando dados de chamados da Netflix
    data = {
        'Ticket_ID': [101, 102, 103, 104, 105],
        'Assunto': ['Login', 'Cobrança', 'Login', 'Streaming Lento', 'Login'],
        'Status': ['Resolvido', 'Pendente', 'Resolvido', 'Resolvido', 'Aberto']
    }
    
    df = pd.DataFrame(data)
    
    # Conta quantos chamados tem de cada tipo
    resumo = df['Assunto'].value_counts()
    
    print("📈 Análise de Chamados de Suporte:")
    print(resumo)
    
    # Exporta o resumo
    df.to_excel("analise_suporte_algar.xlsx", index=False)
    print("\n✅ Resumo exportado para o RH/Gestão.")

analyze_tickets()