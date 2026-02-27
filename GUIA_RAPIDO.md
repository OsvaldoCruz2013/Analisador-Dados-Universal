# 🚀 GUIA RÁPIDO DE USO

## ⚡ Início Rápido

### Método 1: Executar o Dashboard (RECOMENDADO) 🌟

**Windows:**

```bash
# Basta clicar duas vezes no arquivo:
run_dashboard.bat

# Ou executar no terminal:
C:\Users\Windows\Desktop\testeSkill\run_dashboard.bat
```

**Bash/Git Bash:**

```bash
./run_dashboard.sh
```

O dashboard abrirá automaticamente no navegador em: `http://localhost:8501`

---

### Método 2: Análise em Terminal

Execute o script de análise exploratória:

```bash
# Ativar o ambiente virtual
C:\Users\Windows\Desktop\testeSkill\.venv\Scripts\activate

# Executar a análise
python analise_dados.py
```

Isso gerará um relatório completo no terminal com:

- ✅ Informações básicas do dataset
- 👥 Análise demográfica
- 💰 Análise financeira
- 📈 Análise de comportamento
- 🔗 Correlações
- 🎯 Segmentação de clientes
- 💡 Insights principais

---

## 📂 Arquivo de Dados

**Localização atual:** `D:\PYTHON\curso_hashtag\materiais\ClientesBanco.csv`

### Para usar um arquivo diferente:

1. **No Dashboard**: Use o campo "Caminho do arquivo CSV" na barra lateral
2. **No script Python**: Edite a variável `caminho` em `analise_dados.py`

---

## 🎯 Funcionalidades Principais do Dashboard

### 🔍 Filtros Disponíveis (Barra Lateral)

- **Categoria de Cartão**: Blue, Gold, Silver, etc.
- **Faixa Etária**: Use o slider para selecionar
- **Sexo**: Masculino, Feminino ou Todos

### 📊 5 Abas de Análise

1. **📊 Visão Geral**
   - Métricas principais
   - Distribuições básicas
   - Dados brutos completos

2. **👥 Perfil Demográfico**
   - Idade, sexo, educação
   - Estado civil, dependentes
   - Análises cruzadas

3. **💰 Análise Financeira**
   - Limites de crédito
   - Faixas salariais
   - Taxa de utilização
   - Volume de transações

4. **📈 Comportamento**
   - Tempo como cliente
   - Produtos contratados
   - Atividade e engajamento
   - Padrões de transações

5. **🎯 Insights & Segmentação**
   - Matriz de segmentação
   - Clientes de alto valor
   - Clientes em risco
   - Oportunidades de cross-sell
   - Correlações

---

## 🛑 Parar o Dashboard

Para parar o servidor Streamlit:

- Pressione `Ctrl + C` no terminal
- Ou feche a janela do terminal

---

## 💡 Dicas de Uso

### Exportar Dados Filtrados

No dashboard, após aplicar filtros, você pode:

- Copiar os dados da tabela
- Fazer screenshots dos gráficos

### Melhor Experiência

- **Tela cheia**: Pressione `F11` no navegador
- **Modo escuro**: Use as configurações do Streamlit (⚙️ no canto superior direito)
- **Atualizar dados**: Use `Ctrl + R` ou `F5` no navegador

### Performance

- O primeiro carregamento pode demorar alguns segundos
- Após o cache, a navegação é instantânea
- Para datasets muito grandes (>100k linhas), considere filtrar os dados

---

## 📊 Exemplos de Insights Possíveis

Com este dashboard você pode responder perguntas como:

✅ **Demográficas:**

- Qual a idade média dos clientes?
- Como se distribui o nível educacional?
- Quantos dependentes os clientes têm em média?

✅ **Financeiras:**

- Qual a faixa salarial predominante?
- Qual a taxa média de utilização do cartão?
- Quanto é o limite médio por categoria de cartão?

✅ **Comportamentais:**

- Quantos produtos os clientes contratam em média?
- Qual o nível de inatividade dos clientes?
- Como variam as transações por faixa etária?

✅ **Estratégicas:**

- Quem são os clientes de alto valor?
- Quais clientes estão em risco de churn?
- Onde estão as oportunidades de cross-sell?

---

## 🆘 Solução de Problemas

### Erro: "ModuleNotFoundError"

```bash
# Reinstale as dependências
C:\Users\Windows\Desktop\testeSkill\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### Erro: "Arquivo não encontrado"

- Verifique se o caminho `D:\PYTHON\curso_hashtag\materiais\ClientesBanco.csv` está correto
- Use o campo de texto na barra lateral para corrigir o caminho

### Dashboard não abre

- Aguarde alguns segundos após executar o comando
- Abra manualmente: `http://localhost:8501`
- Verifique se a porta 8501 não está em uso

### Performance lenta

- Feche outras abas do navegador
- Reduza os filtros para trabalhar com menos dados
- Reinicie o dashboard

---

## 📚 Recursos Adicionais

### Documentação

- **Pandas**: https://pandas.pydata.org/docs/
- **Streamlit**: https://docs.streamlit.io/
- **Plotly**: https://plotly.com/python/

### Skills Instalados

Consulte: `.agents/skills/pandas-data-analysis/SKILL.md`

---

## ✨ Próximos Passos

Depois de explorar os dados, você pode:

1. **Exportar insights** para apresentações
2. **Adicionar novas visualizações** editando `app_streamlit.py`
3. **Criar modelos preditivos** (ex: previsão de churn)
4. **Automatizar relatórios** agendando o script `analise_dados.py`
5. **Integrar com bancos de dados** para dados em tempo real

---

**🎉 Aproveite sua análise de dados!**
