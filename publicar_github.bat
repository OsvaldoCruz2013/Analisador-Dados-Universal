@echo off
REM ========================================================================
REM  PUBLICAR NO GITHUB - Script Automatizado
REM ========================================================================

echo.
echo ========================================================================
echo   PUBLICANDO PROJETO NO GITHUB
echo ========================================================================
echo.

REM Verificar se jรก tem remote configurado
git remote -v > nul 2>&1
if %errorlevel% neq 0 (
    echo [ERRO] Git nao esta inicializado neste projeto!
    echo Execute primeiro: git init
    pause
    exit /b 1
)

REM Solicitar informações do repositório
echo Por favor, forneca as informacoes do seu repositorio GitHub:
echo.
set /p GITHUB_USER="Seu usuario do GitHub: "
set /p REPO_NAME="Nome do repositorio (ex: dashboard-analise-bancaria): "

echo.
echo Configurando repositorio remoto...
git remote remove origin 2>nul
git remote add origin https://github.com/%GITHUB_USER%/%REPO_NAME%.git

echo.
echo Adicionando arquivos...
git add .

echo.
echo Fazendo commit...
set /p COMMIT_MSG="Mensagem do commit (Enter para usar padrao): "
if "%COMMIT_MSG%"=="" set COMMIT_MSG=Atualizacao do projeto

git commit -m "%COMMIT_MSG%"

echo.
echo Enviando para o GitHub...
git branch -M main
git push -u origin main

echo.
echo ========================================================================
echo   CONCLUIDO!
echo ========================================================================
echo.
echo Seu projeto foi publicado em:
echo https://github.com/%GITHUB_USER%/%REPO_NAME%
echo.
echo Proximos passos:
echo 1. Acessar https://share.streamlit.io
echo 2. Fazer login com GitHub
echo 3. Criar novo app apontando para seu repositorio
echo 4. Aguardar deploy (2-5 minutos)
echo.
pause
