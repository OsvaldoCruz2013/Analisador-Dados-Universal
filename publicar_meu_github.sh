#!/bin/bash
# ========================================================================
#  PUBLICAR PROJETO NO GITHUB - analisador-dados-universal
# ========================================================================

echo ""
echo "========================================================================"
echo "   PUBLICAR NO GITHUB - Analisador Universal de Dados CSV"
echo "========================================================================"
echo ""
echo "Seu usuário: OsvaldoCruz2013"
echo "Repositório: analisador-dados-universal"
echo ""
echo "========================================================================"
echo "   PASSO 1: CRIAR REPOSITÓRIO NO GITHUB"
echo "========================================================================"
echo ""
echo "1. Acesse: https://github.com/new"
echo "2. Repository name: analisador-dados-universal"
echo "3. Description: Dashboard interativo para análise de qualquer arquivo CSV com detecção automática de tipos"
echo "4. Escolha: Public (recomendado para portfólio)"
echo "5. NÃO marque 'Add a README file'"
echo "6. NÃO marque 'Add .gitignore'"
echo "7. Clique em 'Create repository'"
echo ""
read -p "Pressione ENTER após criar o repositório..."

echo ""
echo "========================================================================"
echo "   PASSO 2: CONFIGURAR E ENVIAR CÓDIGO"
echo "========================================================================"
echo ""

# Adicionar remote
echo "[1/3] Configurando remote do GitHub..."
git remote remove origin 2>/dev/null
git remote add origin https://github.com/OsvaldoCruz2013/analisador-dados-universal.git
if [ $? -ne 0 ]; then
    echo "ERRO: Falha ao adicionar remote"
    exit 1
fi
echo "✓ OK - Remote configurado!"
echo ""

# Verificar status
echo "[2/3] Verificando commits..."
git log --oneline -3
echo ""

# Push para GitHub
echo "[3/3] Enviando código para GitHub..."
echo ""
echo "IMPORTANTE: Digite seu token de acesso pessoal (Personal Access Token)"
echo "quando solicitar a senha."
echo ""
echo "Como criar um token:"
echo "1. Vá em: https://github.com/settings/tokens"
echo "2. Clique em 'Generate new token (classic)'"
echo "3. Marque 'repo' (full control of private repositories)"
echo "4. Copie o token gerado"
echo ""
read -p "Pressione ENTER para continuar..."

git push -u origin main
if [ $? -ne 0 ]; then
    echo ""
    echo "ERRO ao fazer push. Verifique:"
    echo "1. Token de acesso está correto"
    echo "2. Repositório foi criado no GitHub"
    echo "3. Repositório tem o nome correto: analisador-dados-universal"
    exit 1
fi

echo ""
echo "========================================================================"
echo "   ✅ SUCESSO! Projeto publicado no GitHub"
echo "========================================================================"
echo ""
echo "URL do repositório:"
echo "https://github.com/OsvaldoCruz2013/analisador-dados-universal"
echo ""
echo "========================================================================"
echo "   PRÓXIMO PASSO: DEPLOY NO STREAMLIT CLOUD"
echo "========================================================================"
echo ""
echo "1. Acesse: https://share.streamlit.io/"
echo "2. Faça login com sua conta GitHub"
echo "3. Clique em 'New app'"
echo "4. Selecione:"
echo "   - Repository: OsvaldoCruz2013/analisador-dados-universal"
echo "   - Branch: main"
echo "   - Main file path: app_universal.py"
echo "5. Clique em 'Deploy!'"
echo ""
echo "Seu app ficará online em:"
echo "https://analisador-dados-universal.streamlit.app"
echo "(ou similar)"
echo ""
echo "Veja o guia completo em: DEPLOY_GITHUB_STREAMLIT.md"
echo ""
