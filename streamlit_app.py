"""
Streamlit Cloud - Ponto de Entrada Principal
Executa o Analisador Universal de Dados CSV
"""

# Este arquivo serve como ponto de entrada padrão para o Streamlit Cloud
# Importa e executa o app_universal.py

import sys
from pathlib import Path

# Garantir que o diretório atual está no path
sys.path.insert(0, str(Path(__file__).parent))

# Importar e executar o app universal
import app_universal

# O Streamlit executará automaticamente o código do módulo importado
