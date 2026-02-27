=============================================================================
GUIA COMPLETO: PUBLICAR NO GITHUB E STREAMLIT CLOUD
=============================================================================

Este guia vai te ensinar a:

1. Publicar seu projeto no GitHub
2. Hospedar o dashboard online GRATUITAMENTE no Streamlit Cloud

=============================================================================
PARTE 1: PUBLICAR NO GITHUB
=============================================================================

## ✅ PASSO 1: Criar Repositório no GitHub

1. Acesse: https://github.com
2. Faça login na sua conta (ou crie uma conta gratuita)
3. Clique no botão "+" no canto superior direito
4. Selecione "New repository"
5. Preencha:
   - Repository name: dashboard-analise-bancaria (ou outro nome)
   - Description: Dashboard interativo para análise de dados bancários
   - Visibilidade: Public (para usar o Streamlit Cloud gratuito)
   - ❌ NÃO marque "Add a README file" (já temos um)
6. Clique em "Create repository"

## ✅ PASSO 2: Conectar Repositório Local ao GitHub

Você verá uma página com instruções. Copie o link do repositório que
aparece algo como: https://github.com/SEU_USUARIO/dashboard-analise-bancaria

No terminal do seu projeto, execute:

cd C:\Users\Windows\Desktop\testeSkill

git remote add origin https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git

git branch -M main

git push -u origin main

Quando solicitado, insira suas credenciais do GitHub.

## ✅ PASSO 3: Verificar no GitHub

1. Atualize a página do seu repositório no GitHub
2. Você deve ver todos os arquivos do projeto!

=============================================================================
PARTE 2: PUBLICAR NO STREAMLIT CLOUD (GRÁTIS!)
=============================================================================

O Streamlit Cloud é GRATUITO e permite hospedar seu dashboard online!

## ✅ PASSO 1: Acessar o Streamlit Cloud

1. Acesse: https://share.streamlit.io
2. Clique em "Sign in" ou "Get started"
3. Selecione "Continue with GitHub"
4. Autorize o Streamlit Cloud a acessar sua conta do GitHub
5. Conceda acesso ao repositório que você criou

## ✅ PASSO 2: Criar Nova Aplicação

1. No painel do Streamlit Cloud, clique em "New app"
2. Preencha as informações:

   Repository: SEU_USUARIO/dashboard-analise-bancaria
   Branch: main
   Main file path: app_streamlit.py

3. Clique em "Deploy!"

## ✅ PASSO 3: Aguardar o Deploy

O Streamlit Cloud vai:

- Instalar todas as dependências do requirements.txt
- Subir seu dashboard
- Gerar uma URL pública para você!

Isso leva de 2 a 5 minutos na primeira vez.

## ✅ PASSO 4: Acessar Seu Dashboard Online

Quando o deploy terminar, você receberá uma URL como:

https://SEU_USUARIO-dashboard-analise-bancaria-app-streamlit-main.streamlit.app

🎉 PRONTO! Seu dashboard está ONLINE e ACESSÍVEL PARA QUALQUER PESSOA!

=============================================================================
PARTE 3: USAR O DASHBOARD ONLINE
=============================================================================

Como não temos o arquivo local (D:\PYTHON\...) online, o dashboard
agora permite UPLOAD DE ARQUIVO!

Para usar:

1. Acesse a URL do seu dashboard
2. Na barra lateral, selecione "Upload de Arquivo"
3. Faça upload do arquivo ClientesBanco.csv
4. O dashboard carregará automaticamente!

Você pode compartilhar a URL com qualquer pessoa. Cada visitante
pode fazer upload do próprio arquivo CSV para análise.

=============================================================================
PARTE 4: ATUALIZAR O PROJETO
=============================================================================

Sempre que fizer mudanças no código:

cd C:\Users\Windows\Desktop\testeSkill

git add .

git commit -m "Descrição das mudanças"

git push

O Streamlit Cloud detecta automaticamente e faz REDEPLOY em minutos!

=============================================================================
PARTE 5: CONFIGURAÇÕES AVANÇADAS (OPCIONAL)
=============================================================================

## 🔒 ADICIONAR DADOS DE EXEMPLO

Se quiser incluir um arquivo CSV de exemplo no repositório:

1. Crie uma pasta "data" no projeto
2. Adicione um arquivo exemplo (menor, sem dados sensíveis)
3. Modifique o app_streamlit.py para carregar por padrão

   git add data/
   git commit -m "Adiciona dados de exemplo"
   git push

## 🎨 PERSONALIZAR URL

No Streamlit Cloud:

1. Vá em "Settings" do app
2. Em "General", você pode alterar o nome do app
3. A URL será atualizada

## 📧 ADICIONAR SECRETS (senhas, API keys)

Se precisar de credenciais:

1. No Streamlit Cloud, vá em "Settings" > "Secrets"
2. Adicione variáveis em formato TOML
3. No código, acesse com: st.secrets["NOME_DA_VARIAVEL"]

=============================================================================
TROUBLESHOOTING (SOLUÇÃO DE PROBLEMAS)
=============================================================================

❌ Erro: "ModuleNotFoundError"
Solução: Certifique-se de que requirements.txt está completo
Adicione módulos faltantes e faça git push

❌ Dashboard não carrega
Solução: Veja os logs no Streamlit Cloud (botão "Manage app" > "Logs")
Verifique erros e corrija

❌ Arquivo muito grande
Solução: O GitHub tem limite de 100MB por arquivo
Use Git LFS ou hospede dados separadamente

❌ Deploy travado
Solução: No Streamlit Cloud, clique em "Reboot app"
Se persistir, delete e crie novo deploy

❌ Git pede senha toda vez
Solução: Configure SSH ou Personal Access Token do GitHub
https://docs.github.com/en/authentication

=============================================================================
RECURSOS ÚTEIS
=============================================================================

📚 Documentação:

- Streamlit Cloud: https://docs.streamlit.io/streamlit-community-cloud
- GitHub: https://docs.github.com
- Git: https://git-scm.com/doc

🎥 Tutoriais em Vídeo:

- Deploy Streamlit Cloud: https://youtu.be/HKoOBiAaHGg
- Git e GitHub: https://youtube.com/github

🤝 Comunidade:

- Streamlit Forum: https://discuss.streamlit.io
- Discord Streamlit: https://discord.gg/streamlit

=============================================================================
CHECKLIST FINAL
=============================================================================

Antes de publicar, verifique:

✅ requirements.txt está completo
✅ .gitignore não ignora arquivos importantes
✅ README_GITHUB.md está atualizado
✅ Código funciona localmente
✅ Não há senhas ou dados sensíveis no código
✅ Repositório no GitHub é "Public"
✅ app_streamlit.py permite upload de arquivo

=============================================================================
PRÓXIMOS PASSOS DEPOIS DO DEPLOY
=============================================================================

1. ⭐ Peça para amigos darem "Star" no GitHub
2. 📝 Atualize o README com a URL do dashboard online
3. 💼 Adicione no LinkedIn/Portfólio
4. 🐦 Compartilhe nas redes sociais
5. 📊 Monitore uso no Streamlit Cloud Analytics

=============================================================================

🎉 PARABÉNS! Você agora tem um dashboard profissional online!

Link do Streamlit Cloud: https://share.streamlit.io
Link do seu GitHub: https://github.com/SEU_USUARIO

=============================================================================
