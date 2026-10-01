# ☕ Projeto de Governança, Qualidade e Limpeza de Dados - Cafeteria

Repositório desenvolvido com foco em **Governança de Dados**, **Data Quality** e **Padronização de Processos**, simulando um cenário real de tratamento de bases de dados desestruturadas em uma cafeteria artesanal.

---

## 🎯 Objetivo do Projeto
Demonstrar a aplicação de boas práticas de governança de dados — desde a especificação técnica em dicionários de dados até a automação da limpeza e validação de registros utilizando **Python (Pandas)**, garantindo confiabilidade e padronização para análises futuras.

---

## 📂 Estrutura do Repositório

```text
governanca-dados-cafeteria/
│
├── dados_brutos/
│   └── dados_brutos_cafe.csv      # Base original contendo inconsistências e erros proposituais.
│
├── dados_tratados/
│   └── dados_tratados_cafe.csv    # Base final limpa, auditada e padronizada.
│
├── documentacao/
│   └── dicionario_de_dados.md     # Especificação técnica das colunas e regras de negócio.
│
└── scripts/
    └── limpeza_dados.py           # Script automatizado de tratamento em Python (Pandas).
```

---

## 🛠️ Tecnologias e Ferramentas Utilizadas

- Python & Pandas (Tratamento, manipulação e automação de dados)

- Markdown (Documentação estruturada)

- Git & GitHub (Controle de versão e portfólio)

---

## 🔍 Problemas Identificados na Base Bruta

Durante a auditoria inicial da base, foram mapeadas as seguintes inconsistências:

- **Nomes de Clientes:** Registros vazios, abreviações incorretas e falta de padronização em letras maiúsculas/minúsculas.

- **Datas:** Mistura entre o padrão brasileiro (`DD/MM/YYYY`) e o internacional (`YYYY-MM-DD`).

- **Tipos de Dados e Unidades:** Colunas numéricas (como peso e valor) misturadas com caracteres textuais (ex: `250g`, `R$`).

- **Valores Categóricos:** Grafias divergentes para um mesmo produto e ausência de padronização nos status de pagamento.

---

## 💡 Sobre o Projeto e Aprendizados

Este projeto foi desenvolvido com o principal intuito de estudar e aplicar conceitos fundamentais de **Governança e Qualidade de Dados** em um cenário prático. Através da construção deste repositório, foi possível vivenciar os desafios reais que envolvem a estruturação de dados desorganizados e entender como a governança impacta diretamente a confiabilidade da informação.

### O que aprendi na prática:
- **Especificação Técnica:** Como estruturar um **Dicionário de Dados** e um **Glossário de Negócio**, definindo claramente tipos de dados, obrigatoriedade de campos e regras empresariais.

- **Diagnóstico de Anomalias:** A identificar padrões de erro comuns em bases brutas, como inconsistências de formatação, divergências entre padrões regionais (brasileiro vs. internacional) e dados ausentes (`NaN`).

- **Automação de Limpeza com Python:** A utilização da biblioteca **Pandas** para aplicar transformações programáticas, utilizando parâmetros avançados (como `format='mixed'`, `dayfirst=True` e `errors='coerce'`) para blindar o código contra falhas de conversão.

- **Visão Sistêmica:** Compreender a importância de manter um pipeline documentado e auditável, garantindo que a base de dados transite do "caos" bruto para um formato confiável e pronto para uso analítico.

---

## 👩‍💻 Autora

Bianca Inazumi
