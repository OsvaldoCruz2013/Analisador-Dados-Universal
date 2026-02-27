#!/bin/bash
# ========================================================================
#  PUBLICAR NO GITHUB - Script Automatizado
# ========================================================================

echo ""
echo "========================================================================"
echo "  PUBLICANDO PROJETO NO GITHUB"
echo "========================================================================"
echo ""

# Verificar se git está inicializado
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo "[ERRO] Git não está inicializado neste projeto!"
    echo "Execute primeiro: git init"
    exit 1
fi

# Solicitar informações do repositório
echo "Por favor, forneça as informações do seu repositório GitHub:"
echo ""
read -p "Seu usuário do GitHub: " GITHUB_USER
read -p "Nome do repositório (ex: dashboard-analise-bancaria): " REPO_NAME

echo ""
echo "Configurando repositório remoto..."
git remote remove origin 2>/dev/null
git remote add origin https://github.com/$GITHUB_USER/$REPO_NAME.git

echo ""
echo "Adicionando arquivos..."
git add .

echo ""
read -p "Mensagem do commit (Enter para usar padrão): " COMMIT_MSG
if [ -z "$COMMIT_MSG" ]; then
    COMMIT_MSG="Atualização do projeto"
fi

git commit -m "$COMMIT_MSG"

echo ""
echo "Enviando para o GitHub..."
git branch -M main
git push -u origin main

echo ""
echo "========================================================================"
echo "  CONCLUÍDO!"
echo "========================================================================"
echo ""
echo "Seu projeto foi publicado em:"
echo "https://github.com/$GITHUB_USER/$REPO_NAME"
echo ""
echo "Próximos passos:"
echo "1. Acessar https://share.streamlit.io"
echo "2. Fazer login com GitHub"
echo "3. Criar novo app apontando para seu repositório"
echo "4. Aguardar deploy (2-5 minutos)"
echo ""
