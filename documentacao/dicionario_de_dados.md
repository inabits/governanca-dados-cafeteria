# Dicionário de Dados - Projeto Cafeteria ☕

Este documento descreve a estrutura técnica e as regras de negócio de cada campo presente na base de dados de pedidos da cafeteria.

## Tabela: `dados_brutos_cafe.csv`

| Coluna | Tipo de Dado | Obrigatório? (Sim/Não) | Regra de Negócio / Padrão Esperado |
| :--- | :--- | :--- | :--- |
| **id_pedido** | Inteiro (INT) | Sim | Identificador único e sequencial de cada pedido realizado. Não pode se repetir ou ser nulo. |
| **nome_cliente** | Texto (String) | Sim | Nome completo do cliente. Deve ser padronizado sem abreviações e sem erros de digitação (Ex: "Ana Souza", e não "A. Souza"). |
| **data_pedido** | Data (YYYY-MM-DD) | Sim | Data em que o pedido foi efetuado. O formato oficial padrão aceito é o internacional `AAAA-MM-DD`. |
| **produto_cafe** | Texto (String) | Sim | Nome comercial do produto de café adquirido. Deve seguir a tabela oficial de produtos da marca. |
| **peso_g** | Inteiro ou Texto | Sim | Peso da embalagem do café em gramas (Ex: `250` ou `500`). Não deve conter letras misturadas no campo numérico. |
| **tipo_moagem** | Texto (String) | Sim | Indica o estado de moagem do grão. Valores permitidos: `Grão` (ou Em grão), `Moído` e `Pó`. |
| **valor_pago** | Numérico (Float) | Sim | Valor monetário total pago pelo pedido. Deve conter apenas números e ponto decimal (Ex: `35.00`), sem o símbolo de moeda. |
| **status_pagamento**| Texto (String) | Sim | Situação atual da transação financeira. Valores permitidos: `Pago`, `Pendente`, `Aprovado` ou `Cancelado`. |