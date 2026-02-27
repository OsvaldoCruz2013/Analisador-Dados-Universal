"""
Redirecionamento para o Analisador Universal de Dados CSV
Este arquivo existe para compatibilidade com deploys antigos do Streamlit Cloud
"""

# Importar e executar o app universal
import sys
from pathlib import Path

# Garantir que o diretório atual está no path
sys.path.insert(0, str(Path(__file__).parent))

# Importar e executar o app_universal
import app_universal

# O Streamlit executará automaticamente o código do módulo importado
