@echo off
REM ========================================================================
REM  DASHBOARD UNIVERSAL - Analisador de Qualquer CSV
REM ========================================================================

echo.
echo ========================================================================
echo   DASHBOARD UNIVERSAL DE ANALISE DE DADOS
echo ========================================================================
echo.
echo Iniciando dashboard que analisa QUALQUER arquivo CSV...
echo.
echo O dashboard abrira automaticamente no navegador em:
echo http://localhost:8502
echo.
echo Para parar o servidor, pressione Ctrl+C
echo.

C:\Users\Windows\Desktop\testeSkill\.venv\Scripts\python.exe -m streamlit run app_universal.py --server.port 8502

pause
