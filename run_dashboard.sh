#!/bin/bash
# Script para executar o dashboard Streamlit
echo "Iniciando Dashboard de Análise de Clientes Bancários..."
echo ""

# Executar Streamlit usando o Python do ambiente virtual
.venv/Scripts/python.exe -m streamlit run app_streamlit.py
