# 📊 Analisador Universal de Dados CSV

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io)
[![GitHub](https://img.shields.io/badge/GitHub-OsvaldoCruz2013-181717?logo=github)](https://github.com/OsvaldoCruz2013/Analisador-Dados-Universal)
![Python](https://img.shields.io/badge/Python-3.14+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31.0-red.svg)
![Pandas](https://img.shields.io/badge/Pandas-2.2.0-green.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

Dashboard interativo para análise de dados desenvolvido com Python, Pandas e Streamlit. **Duas versões disponíveis**: analisador universal genérico para qualquer CSV e análise bancária especializada.

---

## ⭐ ESCOLHA SUA VERSÃO

### 🏦 Dashboard Bancário (Específico)

- **Arquivo**: `app_streamlit.py`
- **Uso**: Análise especializada de dados bancários
- **Executar**: `run_dashboard.bat` (Windows) ou `run_dashboard.sh` (Linux/Mac)
- Visualizações especializadas para dados bancários
- Colunas pré-configuradas (CLIENTNUM, Categoria Cartão, etc.)

### 📊 Dashboard Universal (Genérico) ⭐ NOVO!

- **Arquivo**: `app_universal.py`
- **Uso**: Analisa **QUALQUER** arquivo CSV automaticamente
- **Executar**: `run_universal.bat` (Windows) ou `run_universal.sh` (Linux/Mac)
- **Detecção automática** de tipos de dados (numérico, categórico, data, booleano)
- **Filtros dinâmicos** baseados nos dados
- **6 abas de análise**: Visão Geral, Numéricas, Categóricas, Cruzada, Temporal, Insights
- Funciona com vendas, RH, financeiro, marketing, saúde, educação, etc.

📖 **[Veja documentação completa do Dashboard Universal →](README_UNIVERSAL.md)**

---

## 🚀 Demo Online

**[Acesse o Dashboard Online](SEU_LINK_AQUI)** _(após deploy no Streamlit Cloud)_

## 📊 Sobre o Projeto

Sistema completo de análise de dados bancários com visualizações interativas que permite:

- **Análise Demográfica**: Perfil dos clientes por idade, sexo, educação, estado civil
- **Análise Financeira**: Limites de crédito, faixas salariais, taxa de utilização
- **Análise de Comportamento**: Produtos contratados, transações, engajamento
- **Segmentação Inteligente**: Identificação de clientes de alto valor, em risco e oportunidades
- **Insights Automáticos**: Correlações e padrões nos dados

## 🎯 Funcionalidades

### 📈 5 Abas de Análise Completa

1. **Visão Geral** - Métricas principais e distribuições básicas
2. **Perfil Demográfico** - Análise de características dos clientes
3. **Análise Financeira** - Limites, transações e utilização de crédito
4. **Comportamento** - Padrões de uso e engajamento
5. **Insights & Segmentação** - Análises avançadas e correlações

### 🔍 Filtros Interativos

- Categoria de Cartão (Blue, Gold, Silver)
- Faixa Etária (slider dinâmico)
- Sexo (Masculino/Feminino/Todos)

### 💡 Insights Automáticos

- ✅ Perfil do cliente típico
- ✅ Clientes de alto valor (top 25%)
- ✅ Clientes em risco de churn
- ✅ Oportunidades de cross-sell
- ✅ Matriz de correlações

## 🛠️ Tecnologias Utilizadas

- **Python 3.14+**
- **Streamlit** - Framework para dashboards interativos
- **Pandas** - Manipulação e análise de dados
- **Plotly** - Visualizações interativas
- **NumPy** - Operações numéricas
- **Seaborn & Matplotlib** - Visualizações estatísticas

## 📦 Instalação Local

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passo a Passo

```bash
# Clone o repositório
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
cd SEU_REPOSITORIO

# Crie um ambiente virtual (recomendado)
python -m venv .venv

# Ative o ambiente virtual
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

# Instale as dependências
pip install -r requirements.txt

# Execute o dashboard
streamlit run app_streamlit.py
```

O dashboard abrirá automaticamente em `http://localhost:8501`

## 📂 Estrutura do Projeto

```
├── streamlit_app.py          # Ponto de entrada Streamlit Cloud
├── app_universal.py          # Analisador universal CSV
├── app_streamlit.py          # Dashboard bancário
├── scripts/
│   └── analise_dados.py      # Script de análise (terminal)
├── requirements.txt          # Dependências Python
├── runtime.txt               # Versão Python (3.11)
├── .streamlit/
│   └── config.toml          # Configuração visual do Streamlit
├── .agents/
│   └── skills/              # Pandas Data Analysis skill
├── README.md                # Este arquivo
├── GUIA_RAPIDO.md          # Guia de uso rápido
└── COMO_USAR.txt           # Instruções detalhadas
```

## 🎮 Como Usar

### Dashboard Online

1. Acesse o link do dashboard
2. Use os filtros na barra lateral para explorar os dados
3. Navigate pelas 5 abas para visualizar diferentes análises
4. Faça upload do seu próprio arquivo CSV (opcional)

### Dashboard Local

1. Execute o script de análise em terminal:

   ```bash
   python scripts/analise_dados.py
   ```

2. Ou execute o dashboard interativo:
   ```bash
   streamlit run app_streamlit.py
   ```

## 📊 Formato dos Dados

O dashboard espera um arquivo CSV com as seguintes colunas:

- **CLIENTNUM**: ID do cliente
- **Idade**: Idade do cliente
- **Sexo**: M ou F
- **Dependentes**: Número de dependentes
- **Educação**: Nível educacional
- **Estado Civil**: Estado civil
- **Faixa Salarial Anual**: Faixa de renda
- **Categoria Cartão**: Blue, Gold, Silver, etc.
- **Meses como Cliente**: Tempo de relacionamento
- **Produtos Contratados**: Quantidade de produtos
- **Limite**: Limite de crédito
- **Taxa de Utilização Cartão**: % de utilização
- **Valor Transacoes 12m**: Volume de transações
- **Qtde Transacoes 12m**: Quantidade de transações
- E outras métricas comportamentais...

## 🚀 Deploy no Streamlit Cloud

Este projeto está pronto para deploy no Streamlit Cloud:

1. Faça fork deste repositório
2. Acesse [share.streamlit.io](https://share.streamlit.io)
3. Conecte seu repositório GitHub
4. O deploy será automático!

## 📈 Exemplos de Insights

Com este dashboard você pode responder:

- Qual a idade média dos clientes?
- Qual a taxa média de utilização do cartão por categoria?
- Quantos clientes estão em risco de churn?
- Onde estão as melhores oportunidades de cross-sell?
- Qual a correlação entre limite e volume de transações?

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abrir um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👨‍💻 Autor

Desenvolvido com ❤️ usando Pandas e Streamlit.

## 🎓 Skill Utilizado

Este projeto utiliza o **Pandas Data Analysis skill** do [Plugin Agent Marketplace](https://github.com/pluginagentmarketplace/custom-plugin-python).

---

**⭐ Se este projeto foi útil para você, considere dar uma estrela!**
