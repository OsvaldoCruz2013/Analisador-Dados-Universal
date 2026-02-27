# 📊 Analisador Universal de Dados CSV

## 🎯 NOVO! Versão Universal

Agora você tem **DUAS versões** do dashboard:

### 1. 🏦 Dashboard Bancário (Original)

- **Arquivo**: `app_streamlit.py`
- **Uso**: Análise específica de dados bancários
- **Executar**: `run_dashboard.bat`
- Colunas pré-configuradas para análise bancária
- Visualizações especializadas

### 2. 📊 Dashboard Universal (NOVO!) ⭐

- **Arquivo**: `app_universal.py`
- **Uso**: Analisa QUALQUER arquivo CSV automaticamente
- **Executar**: `run_universal.bat`
- Detecta tipos de dados automaticamente
- Adapta visualizações ao conteúdo
- Funciona com qualquer estrutura de dados

---

## 🚀 Como Usar o Dashboard Universal

### Localmente:

1. **Execute o dashboard:**

   ```
   📌 Duplo clique em: run_universal.bat
   ```

2. **Faça upload do seu CSV:**
   - Arraste e solte seu arquivo
   - Ou clique em "Browse files"
   - Qualquer arquivo CSV funciona!

3. **Explore as análises automáticas:**
   - ✅ Visão Geral
   - ✅ Variáveis Numéricas
   - ✅ Variáveis Categóricas
   - ✅ Análise Cruzada
   - ✅ Análise Temporal
   - ✅ Insights Automáticos

---

## 🎨 Funcionalidades do Dashboard Universal

### 🔍 Detecção Automática

- **Tipos de Dados**: Numérico, categórico, data, booleano, texto
- **Encoding**: UTF-8 e Latin-1 automaticamente
- **Separadores**: Vírgula, ponto-e-vírgula

### 📊 Análises Automáticas

#### Variáveis Numéricas:

- Estatísticas descritivas (média, mediana, desvio padrão)
- Histogramas interativos
- Box plots para detectar outliers
- Matriz de correlação

#### Variáveis Categóricas:

- Distribuição de frequências
- Gráficos de barras e pizza
- Tabelas de proporções

#### Análise Cruzada:

- Comparação entre numérico vs categórico
- Box plots por categoria
- Estatísticas agrupadas

#### Análise Temporal:

- Detecção automática de colunas de data
- Séries temporais
- Agregação por dia/semana/mês/ano
- Tendências ao longo do tempo

#### Insights Automáticos:

- ⚠️ Detecção de valores nulos
- 🔑 Identificação de IDs únicos
- 📊 Detecção de outliers
- ⚖️ Identificação de desbalanceamento
- 🔗 Correlações fortes

### 🔧 Filtros Dinâmicos

- Filtros baseados nas colunas categóricas do seu arquivo
- Seleção múltipla de valores
- Atualização em tempo real

---

## 📁 Exemplos de Uso

O Dashboard Universal funciona com QUALQUER tipo de dados:

### ✅ Vendas:

- data, produto, quantidade, valor, cliente, região

### ✅ RH:

- funcionario, departamento, salario, data_admissao, idade

### ✅ Financeiro:

- data, categoria, receita, despesa, saldo

### ✅ Marketing:

- campanha, canal, clicks, conversoes, custo, data

### ✅ E-commerce:

- pedido, cliente, produto, valor, status, data

### ✅ Saúde:

- paciente, idade, diagnostico, tratamento, data

### ✅ Educação:

- aluno, curso, nota, frequencia, data

---

## 🆚 Comparação das Versões

| Característica | Dashboard Bancário     | Dashboard Universal |
| -------------- | ---------------------- | ------------------- |
| Arquivo        | app_streamlit.py       | app_universal.py    |
| Colunas        | Específicas (bancário) | Qualquer            |
| Detecção       | Manual                 | Automática          |
| Upload         | Sim                    | Sim                 |
| Filtros        | 3 fixos                | Dinâmicos           |
| Abas           | 5 especializadas       | 6 genéricas         |
| Insights       | Bancários              | Gerais              |
| Use quando     | Dados bancários        | Qualquer dado       |

---

## 🌐 Publicar no Streamlit Cloud

### Para Dashboard Universal:

1. **Escolha qual versão publicar:**
   - Bancário: `app_streamlit.py`
   - Universal: `app_universal.py` ⭐ (recomendado para uso geral)

2. **No Streamlit Cloud:**
   - Main file path: `app_universal.py`

3. **Vantagens da versão universal:**
   - Qualquer pessoa pode analisar seus próprios dados
   - Mais flexível e reutilizável
   - Ideal para portfólio

---

## 📊 Estrutura dos Arquivos

```
testeSkill/
│
├── app_streamlit.py       # Dashboard bancário (específico)
├── app_universal.py       # Dashboard universal (genérico) ⭐
│
├── run_dashboard.bat      # Executa versão bancária
├── run_universal.bat      # Executa versão universal ⭐
│
├── analise_dados.py       # Script de análise (bancário)
├── requirements.txt       # Mesmas dependências
└── README.md             # Este arquivo
```

---

## 🎯 Recomendação

**Para publicar online:** Use `app_universal.py`

- Mais flexível
- Funciona com qualquer CSV
- Melhor para portfólio
- Maior audiência potencial

**Para uso específico:** Use `app_streamlit.py`

- Análises especializadas
- Visualizações customizadas
- Insights de domínio específico

---

## 💡 Dicas de Uso

### Upload de Arquivos:

- Máximo 200MB por arquivo
- Use CSV limpo (sem formatações especiais)
- Primeira linha deve ser o cabeçalho

### Performance:

- Arquivos até 10k linhas: Instantâneo
- 10k-100k linhas: Alguns segundos
- 100k+ linhas: Considere filtrar dados antes

### Melhores Práticas:

- Nomear colunas de forma clara
- Evitar caracteres especiais nos nomes
- Use datas no formato ISO (YYYY-MM-DD)
- Mantenha consistência nos dados

---

## 🔧 Personalização

### Adicionar análises específicas:

Edite `app_universal.py` e adicione funções na seção de tabs.

Exemplo:

```python
with tabs[6]:
    st.header("Sua Análise Customizada")
    # Seu código aqui
```

### Mudar portas:

```bash
# Porta diferente
streamlit run app_universal.py --server.port 8503
```

---

## 📚 Recursos

- **Documentação Streamlit**: https://docs.streamlit.io
- **Plotly Graphs**: https://plotly.com/python/
- **Pandas**: https://pandas.pydata.org/docs/

---

## 🆘 Problemas Comuns

**Erro de encoding:**

- O sistema tenta UTF-8 e Latin-1 automaticamente
- Se ainda falhar, converta o CSV para UTF-8

**Muitas colunas:**

- Dashboard suporta até 1000 colunas
- Análises focam nas 50 primeiras por performance

**Datas não detectadas:**

- Use formato padrão: YYYY-MM-DD
- Ou DD/MM/YYYY, MM/DD/YYYY

**Gráfico não aparece:**

- Verifique se há dados suficientes (mínimo 2 registros)
- Verifique valores nulos na coluna

---

## ✨ Próximos Passos

1. **Teste com seus dados**
2. **Escolha qual versão publicar**
3. **Personalize conforme necessário**
4. **Compartilhe com o mundo!**

---

**🎉 Agora você tem um analisador de dados universal e profissional!**
