"""
Streamlit Cloud - Ponto de Entrada Principal  
Executa o Analisador Universal de Dados CSV
"""

# Este arquivo serve como ponto de entrada padrão para o Streamlit Cloud
from app_universal import main
import sys
from pathlib import Path

# Garantir que o diretório atual está no path
sys.path.insert(0, str(Path(__file__).parent))

# Importar e executar o app universal

# Executar a aplicação
main()
