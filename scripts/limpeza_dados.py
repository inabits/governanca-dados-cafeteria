import pandas as pd

# CARREGAR DADOS BRUTOS
df = pd.read_csv('dados_brutos/dados_brutos_cafe.csv')

# PADRONIZAÇÃO DE NOME DO CLIENTE
df['nome_cliente'] = df['nome_cliente'].fillna('Desconhecido')
df['nome_cliente'] = df['nome_cliente'].replace({'A. Souza': 'Ana Souza'})
df['nome_cliente'] = df['nome_cliente'].str.strip().str.title()

# PADRONIZAÇÃO DE DATAS
df['data_pedido'] = pd.to_datetime(df['data_pedido'], format='mixed', dayfirst=True, errors='coerce')
df['data_pedido'] = df['data_pedido'].dt.strftime('%Y-%m-%d')

# PADRONIZAÇÃO DE PESO
df['peso_g'] = df['peso_g'].astype(str).str.replace('g', '', case=False)
df['peso_g'] = pd.to_numeric(df['peso_g'], errors='coerce').astype(int)

# PADRONIZAÇÃO DO TIPO DE MOAGEM
df['tipo_moagem'] = df['tipo_moagem'].astype(str).str.strip().str.lower()
mapa_moagem = {
    'grao': 'Em grão',
    'grão': 'Em grão',
    'em grao': 'Em grão',
    'moido': 'Moído',
    'po': 'Pó',
    'pó': 'Pó'
}
df['tipo_moagem'] = df['tipo_moagem'].map(mapa_moagem)

# PADRONIZAÇÃO DO VALOR PAGO
df['valor_pago'] = df['valor_pago'].astype(str).str.replace('R$', '')
df['valor_pago'] = df['valor_pago'].str.replace(',', '.')
df['valor_pago'] = pd.to_numeric(df['valor_pago'], errors='coerce')

# PADRONIZAÇÃO DO STATUS DE PAGAMENTO
df['status_pagamento'] = df['status_pagamento'].fillna('Pendente')
df['status_pagamento'] = df['status_pagamento'].str.strip().str.capitalize()

# SALVAR DADOS LIMPOS
df.to_csv('dados_tratados/dados_tratados_cafe.csv', index=False)