#!/bin/bash
# ========================================================================
#  DASHBOARD UNIVERSAL - Analisador de Qualquer CSV
# ========================================================================

echo ""
echo "========================================================================"
echo "   DASHBOARD UNIVERSAL DE ANALISE DE DADOS"
echo "========================================================================"
echo ""
echo "Iniciando dashboard que analisa QUALQUER arquivo CSV..."
echo ""
echo "O dashboard abrirá automaticamente no navegador em:"
echo "http://localhost:8502"
echo ""
echo "Para parar o servidor, pressione Ctrl+C"
echo ""

# Ativa o ambiente virtual
source .venv/bin/activate

# Inicia o Streamlit
streamlit run app_universal.py --server.port 8502
