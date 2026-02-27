@echo off
REM ========================================================================
REM  PUBLICAR PROJETO NO GITHUB - analisador-dados-universal
REM ========================================================================

echo.
echo ========================================================================
echo   PUBLICAR NO GITHUB - Analisador Universal de Dados CSV
echo ========================================================================
echo.
echo Seu usuario: OsvaldoCruz2013
echo Repositorio: analisador-dados-universal
echo.
echo ========================================================================
echo   PASSO 1: CRIAR REPOSITORIO NO GITHUB
echo ========================================================================
echo.
echo 1. Acesse: https://github.com/new
echo 2. Repository name: analisador-dados-universal
echo 3. Description: Dashboard interativo para analise de qualquer arquivo CSV com deteccao automatica de tipos
echo 4. Escolha: Public (recomendado para portfolio)
echo 5. NAO marque "Add a README file"
echo 6. NAO marque "Add .gitignore"
echo 7. Clique em "Create repository"
echo.
echo Pressione qualquer tecla apos criar o repositorio...
pause > nul

echo.
echo ========================================================================
echo   PASSO 2: CONFIGURAR E ENVIAR CODIGO
echo ========================================================================
echo.

REM Adicionar remote
echo [1/3] Configurando remote do GitHub...
git remote remove origin 2>nul
git remote add origin https://github.com/OsvaldoCruz2013/analisador-dados-universal.git
if %errorlevel% neq 0 (
    echo ERRO: Falha ao adicionar remote
    pause
    exit /b 1
)
echo OK - Remote configurado!
echo.

REM Verificar status
echo [2/3] Verificando commits...
git log --oneline -3
echo.

REM Push para GitHub
echo [3/3] Enviando codigo para GitHub...
echo.
echo IMPORTANTE: Digite seu token de acesso pessoal (Personal Access Token)
echo quando solicitar a senha.
echo.
echo Como criar um token:
echo 1. Va em: https://github.com/settings/tokens
echo 2. Clique em "Generate new token (classic)"
echo 3. Marque "repo" (full control of private repositories)
echo 4. Copie o token gerado
echo.
pause

git push -u origin main
if %errorlevel% neq 0 (
    echo.
    echo ERRO ao fazer push. Verifique:
    echo 1. Token de acesso esta correto
    echo 2. Repositorio foi criado no GitHub
    echo 3. Repositorio tem o nome correto: analisador-dados-universal
    pause
    exit /b 1
)

echo.
echo ========================================================================
echo   SUCESSO! Projeto publicado no GitHub
echo ========================================================================
echo.
echo URL do repositorio:
echo https://github.com/OsvaldoCruz2013/analisador-dados-universal
echo.
echo ========================================================================
echo   PROXIMO PASSO: DEPLOY NO STREAMLIT CLOUD
echo ========================================================================
echo.
echo 1. Acesse: https://share.streamlit.io/
echo 2. Faca login com sua conta GitHub
echo 3. Clique em "New app"
echo 4. Selecione:
echo    - Repository: OsvaldoCruz2013/analisador-dados-universal
echo    - Branch: main
echo    - Main file path: app_universal.py
echo 5. Clique em "Deploy!"
echo.
echo Seu app ficara online em:
echo https://analisador-dados-universal.streamlit.app
echo (ou similar)
echo.
echo Veja o guia completo em: DEPLOY_GITHUB_STREAMLIT.md
echo.
pause
