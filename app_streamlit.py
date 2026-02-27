"""
Dashboard Streamlit - Análise de Clientes Bancários
Aplicação interativa para exploração e visualização de dados
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Configuração da página
st.set_page_config(
    page_title="Análise de Clientes Bancários",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilo customizado
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        padding: 1rem 0;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
    }
    </style>
""", unsafe_allow_html=True)

@st.cache_data
def carregar_dados(caminho=None, arquivo_upload=None):
    """Carrega e processa os dados"""
    if arquivo_upload is not None:
        df = pd.read_csv(arquivo_upload, encoding='latin-1')
    elif caminho:
        df = pd.read_csv(caminho, encoding='latin-1')
    else:
        return None
    
    # Criar segmentações
    df['Segmento_Idade'] = pd.cut(
        df['Idade'], 
        bins=[0, 30, 40, 50, 100], 
        labels=['Jovem (≤30)', 'Adulto (31-40)', 'Meia-idade (41-50)', 'Sênior (>50)']
    )
    
    df['Segmento_Uso'] = pd.cut(
        df['Taxa de Utilização Cartão'],
        bins=[-0.01, 0.3, 0.6, 1.0],
        labels=['Baixo Uso (<30%)', 'Uso Moderado (30-60%)', 'Alto Uso (>60%)']
    )
    
    df['Segmento_Limite'] = pd.cut(
        df['Limite'],
        bins=[0, 5000, 10000, 20000, float('inf')],
        labels=['Básico (<5k)', 'Intermediário (5k-10k)', 'Premium (10k-20k)', 'VIP (>20k)']
    )
    
    return df

def main():
    """Função principal do dashboard"""
    
    # Cabeçalho
    st.markdown('<h1 class="main-header">🏦 Dashboard de Análise de Clientes Bancários</h1>', unsafe_allow_html=True)
    st.markdown("---")
    
    # Sidebar - Carregar dados
    st.sidebar.title("⚙️ Configurações")
    st.sidebar.markdown("---")
    
    # Opção de upload ou caminho local
    opcao_dados = st.sidebar.radio(
        "📂 Fonte de Dados:",
        ["Upload de Arquivo", "Caminho Local"],
        index=0
    )
    
    df = None
    
    if opcao_dados == "Upload de Arquivo":
        st.sidebar.markdown("**Faça upload do arquivo CSV:**")
        arquivo_upload = st.sidebar.file_uploader(
            "Selecione o arquivo CSV",
            type=['csv'],
            help="Arquivo CSV com dados de clientes bancários"
        )
        
        if arquivo_upload is not None:
            try:
                df = carregar_dados(arquivo_upload=arquivo_upload)
                st.sidebar.success(f"✅ {len(df)} registros carregados")
            except Exception as e:
                st.sidebar.error(f"❌ Erro ao carregar arquivo: {e}")
        else:
            st.info("👆 Por favor, faça upload de um arquivo CSV para começar a análise.")
            st.markdown("""
            ### 📋 Formato Esperado do Arquivo
            
            O arquivo CSV deve conter as seguintes colunas:
            - CLIENTNUM, Idade, Sexo, Dependentes
            - Educação, Estado Civil, Faixa Salarial Anual
            - Categoria Cartão, Meses como Cliente
            - Produtos Contratados, Inatividade 12m
            - Limite, Taxa de Utilização Cartão
            - Valor Transacoes 12m, Qtde Transacoes 12m
            
            **Exemplo de dados:** [ClientesBanco.csv](https://github.com)
            """)
            st.stop()
    
    else:  # Caminho Local
        caminho_padrao = r"D:\PYTHON\curso_hashtag\materiais\ClientesBanco.csv"
        caminho_arquivo = st.sidebar.text_input("📂 Caminho do arquivo CSV:", value=caminho_padrao)
        
        try:
            df = carregar_dados(caminho=caminho_arquivo)
            st.sidebar.success(f"✅ {len(df)} registros carregados")
        except Exception as e:
            st.sidebar.error(f"❌ Erro ao carregar arquivo: {e}")
            st.error(f"Não foi possível carregar o arquivo: {caminho_arquivo}")
            st.stop()
    
    # Filtros na sidebar
    st.sidebar.markdown("---")
    st.sidebar.subheader("🔍 Filtros")
    
    # Filtro de categoria de cartão
    categorias_cartao = ['Todos'] + list(df['Categoria Cartão'].dropna().unique())
    categoria_selecionada = st.sidebar.selectbox("Categoria de Cartão:", categorias_cartao)
    
    # Filtro de faixa etária
    idade_min, idade_max = st.sidebar.slider(
        "Faixa Etária:",
        int(df['Idade'].min()),
        int(df['Idade'].max()),
        (int(df['Idade'].min()), int(df['Idade'].max()))
    )
    
    # Filtro de sexo
    sexos = ['Todos'] + list(df['Sexo'].unique())
    sexo_selecionado = st.sidebar.selectbox("Sexo:", sexos)
    
    # Aplicar filtros
    df_filtrado = df.copy()
    if categoria_selecionada != 'Todos':
        df_filtrado = df_filtrado[df_filtrado['Categoria Cartão'] == categoria_selecionada]
    df_filtrado = df_filtrado[(df_filtrado['Idade'] >= idade_min) & (df_filtrado['Idade'] <= idade_max)]
    if sexo_selecionado != 'Todos':
        df_filtrado = df_filtrado[df_filtrado['Sexo'] == sexo_selecionado]
    
    st.sidebar.markdown(f"**Registros após filtros:** {len(df_filtrado)}")
    
    # Tabs principais
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📊 Visão Geral", 
        "👥 Perfil Demográfico", 
        "💰 Análise Financeira",
        "📈 Comportamento",
        "🎯 Insights & Segmentação"
    ])
    
    # TAB 1: VISÃO GERAL
    with tab1:
        st.header("📊 Visão Geral dos Dados")
        
        # Métricas principais
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric(
                "Total de Clientes",
                f"{len(df_filtrado):,}",
                delta=f"{len(df_filtrado)-len(df)}" if len(df_filtrado) != len(df) else None
            )
        
        with col2:
            st.metric(
                "Idade Média",
                f"{df_filtrado['Idade'].mean():.1f} anos"
            )
        
        with col3:
            st.metric(
                "Limite Médio",
                f"R$ {df_filtrado['Limite'].mean():,.0f}"
            )
        
        with col4:
            st.metric(
                "Taxa Utilização Média",
                f"{df_filtrado['Taxa de Utilização Cartão'].mean():.1%}"
            )
        
        st.markdown("---")
        
        # Gráficos lado a lado
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📋 Distribuição por Categoria de Cartão")
            fig_cartao = px.pie(
                df_filtrado,
                names='Categoria Cartão',
                title='Distribuição de Categorias de Cartão',
                hole=0.4,
                color_discrete_sequence=px.colors.qualitative.Set3
            )
            st.plotly_chart(fig_cartao, use_container_width=True)
        
        with col2:
            st.subheader("👫 Distribuição por Sexo")
            fig_sexo = px.bar(
                df_filtrado['Sexo'].value_counts().reset_index(),
                x='Sexo',
                y='count',
                title='Distribuição por Sexo',
                color='Sexo',
                color_discrete_map={'M': '#1f77b4', 'F': '#ff7f0e'}
            )
            st.plotly_chart(fig_sexo, use_container_width=True)
        
        # Dados brutos
        st.markdown("---")
        st.subheader("📄 Dados Brutos")
        st.dataframe(df_filtrado, use_container_width=True, height=300)
        
        # Estatísticas descritivas
        st.subheader("📈 Estatísticas Descritivas")
        st.dataframe(df_filtrado.describe(), use_container_width=True)
    
    # TAB 2: PERFIL DEMOGRÁFICO
    with tab2:
        st.header("👥 Perfil Demográfico dos Clientes")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Distribuição de idade
            st.subheader("📅 Distribuição de Idade")
            fig_idade = px.histogram(
                df_filtrado,
                x='Idade',
                nbins=30,
                title='Distribuição de Idade dos Clientes',
                color_discrete_sequence=['#1f77b4']
            )
            fig_idade.update_layout(yaxis_title='Quantidade de Clientes')
            st.plotly_chart(fig_idade, use_container_width=True)
            
            # Estado Civil
            st.subheader("💍 Estado Civil")
            fig_estado_civil = px.bar(
                df_filtrado['Estado Civil'].value_counts().reset_index(),
                x='Estado Civil',
                y='count',
                title='Distribuição por Estado Civil',
                color='count',
                color_continuous_scale='blues'
            )
            st.plotly_chart(fig_estado_civil, use_container_width=True)
        
        with col2:
            # Educação
            st.subheader("🎓 Nível de Educação")
            fig_educacao = px.pie(
                df_filtrado,
                names='Educação',
                title='Distribuição por Nível de Educação',
                color_discrete_sequence=px.colors.qualitative.Pastel
            )
            st.plotly_chart(fig_educacao, use_container_width=True)
            
            # Dependentes
            st.subheader("👶 Número de Dependentes")
            fig_dependentes = px.bar(
                df_filtrado['Dependentes'].value_counts().sort_index().reset_index(),
                x='Dependentes',
                y='count',
                title='Distribuição de Dependentes',
                color='count',
                color_continuous_scale='oranges'
            )
            st.plotly_chart(fig_dependentes, use_container_width=True)
        
        # Crosstab Idade x Sexo
        st.markdown("---")
        st.subheader("🔄 Análise Cruzada: Idade por Sexo")
        fig_idade_sexo = px.box(
            df_filtrado,
            x='Sexo',
            y='Idade',
            color='Sexo',
            title='Distribuição de Idade por Sexo',
            color_discrete_map={'M': '#1f77b4', 'F': '#ff7f0e'}
        )
        st.plotly_chart(fig_idade_sexo, use_container_width=True)
    
    # TAB 3: ANÁLISE FINANCEIRA
    with tab3:
        st.header("💰 Análise Financeira")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(
                "💵 Limite Total",
                f"R$ {df_filtrado['Limite'].sum():,.0f}"
            )
        
        with col2:
            st.metric(
                "💳 Limite Consumido Total",
                f"R$ {df_filtrado['Limite Consumido'].sum():,.0f}"
            )
        
        with col3:
            st.metric(
                "💸 Volume Transações (12m)",
                f"R$ {df_filtrado['Valor Transacoes 12m'].sum():,.0f}"
            )
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Distribuição de limite por categoria de cartão
            st.subheader("💳 Limite por Categoria de Cartão")
            fig_limite_cartao = px.box(
                df_filtrado,
                x='Categoria Cartão',
                y='Limite',
                color='Categoria Cartão',
                title='Distribuição de Limite por Categoria',
                color_discrete_sequence=px.colors.qualitative.Set2
            )
            st.plotly_chart(fig_limite_cartao, use_container_width=True)
            
            # Faixa salarial
            st.subheader("💰 Distribuição por Faixa Salarial")
            fig_salario = px.bar(
                df_filtrado['Faixa Salarial Anual'].value_counts().reset_index(),
                x='Faixa Salarial Anual',
                y='count',
                title='Clientes por Faixa Salarial',
                color='count',
                color_continuous_scale='greens'
            )
            st.plotly_chart(fig_salario, use_container_width=True)
        
        with col2:
            # Taxa de utilização
            st.subheader("📊 Taxa de Utilização do Cartão")
            fig_utilizacao = px.histogram(
                df_filtrado,
                x='Taxa de Utilização Cartão',
                nbins=50,
                title='Distribuição da Taxa de Utilização',
                color_discrete_sequence=['#2ca02c']
            )
            st.plotly_chart(fig_utilizacao, use_container_width=True)
            
            # Valor de transações por categoria
            st.subheader("💸 Valor Médio de Transações por Categoria")
            valor_medio = df_filtrado.groupby('Categoria Cartão')['Valor Transacoes 12m'].mean().reset_index()
            fig_valor_transacoes = px.bar(
                valor_medio,
                x='Categoria Cartão',
                y='Valor Transacoes 12m',
                title='Valor Médio de Transações (12 meses)',
                color='Valor Transacoes 12m',
                color_continuous_scale='purples'
            )
            st.plotly_chart(fig_valor_transacoes, use_container_width=True)
        
        # Scatter plot
        st.markdown("---")
        st.subheader("🔍 Relação: Limite vs Valor de Transações")
        fig_scatter = px.scatter(
            df_filtrado,
            x='Limite',
            y='Valor Transacoes 12m',
            color='Categoria Cartão',
            size='Qtde Transacoes 12m',
            hover_data=['Idade', 'Sexo'],
            title='Limite vs Valor de Transações (tamanho = qtde transações)',
            opacity=0.6
        )
        st.plotly_chart(fig_scatter, use_container_width=True)
    
    # TAB 4: COMPORTAMENTO
    with tab4:
        st.header("📈 Análise de Comportamento")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(
                "⏱️ Tempo Médio como Cliente",
                f"{df_filtrado['Meses como Cliente'].mean():.1f} meses"
            )
        
        with col2:
            st.metric(
                "📦 Produtos Médios por Cliente",
                f"{df_filtrado['Produtos Contratados'].mean():.2f}"
            )
        
        with col3:
            st.metric(
                "🔄 Transações Médias (12m)",
                f"{df_filtrado['Qtde Transacoes 12m'].mean():.1f}"
            )
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Produtos contratados
            st.subheader("📦 Distribuição de Produtos Contratados")
            fig_produtos = px.bar(
                df_filtrado['Produtos Contratados'].value_counts().sort_index().reset_index(),
                x='Produtos Contratados',
                y='count',
                title='Número de Produtos por Cliente',
                color='count',
                color_continuous_scale='blues'
            )
            st.plotly_chart(fig_produtos, use_container_width=True)
            
            # Inatividade
            st.subheader("😴 Meses de Inatividade (12m)")
            fig_inatividade = px.bar(
                df_filtrado['Inatividade 12m'].value_counts().sort_index().reset_index(),
                x='Inatividade 12m',
                y='count',
                title='Distribuição de Meses Inativos',
                color='count',
                color_continuous_scale='reds'
            )
            st.plotly_chart(fig_inatividade, use_container_width=True)
        
        with col2:
            # Tempo como cliente
            st.subheader("⏱️ Tempo como Cliente")
            fig_tempo = px.histogram(
                df_filtrado,
                x='Meses como Cliente',
                nbins=30,
                title='Distribuição de Tempo como Cliente',
                color_discrete_sequence=['#9467bd']
            )
            st.plotly_chart(fig_tempo, use_container_width=True)
            
            # Contatos
            st.subheader("📞 Contatos nos Últimos 12 Meses")
            fig_contatos = px.bar(
                df_filtrado['Contatos 12m'].value_counts().sort_index().reset_index(),
                x='Contatos 12m',
                y='count',
                title='Distribuição de Contatos',
                color='count',
                color_continuous_scale='oranges'
            )
            st.plotly_chart(fig_contatos, use_container_width=True)
        
        # Análise de transações
        st.markdown("---")
        st.subheader("💳 Quantidade de Transações por Segmento de Idade")
        transacoes_idade = df_filtrado.groupby('Segmento_Idade')['Qtde Transacoes 12m'].mean().reset_index()
        fig_trans_idade = px.bar(
            transacoes_idade,
            x='Segmento_Idade',
            y='Qtde Transacoes 12m',
            title='Média de Transações por Faixa Etária',
            color='Qtde Transacoes 12m',
            color_continuous_scale='viridis'
        )
        st.plotly_chart(fig_trans_idade, use_container_width=True)
    
    # TAB 5: INSIGHTS & SEGMENTAÇÃO
    with tab5:
        st.header("🎯 Insights e Segmentação")
        
        # Segmentação por idade e uso
        st.subheader("📊 Matriz de Segmentação: Idade vs Uso do Cartão")
        segmentacao = pd.crosstab(
            df_filtrado['Segmento_Idade'],
            df_filtrado['Segmento_Uso'],
            margins=True
        )
        st.dataframe(segmentacao, use_container_width=True)
        
        # Heatmap de segmentação
        fig_heatmap = px.density_heatmap(
            df_filtrado,
            x='Segmento_Idade',
            y='Segmento_Uso',
            title='Heatmap de Segmentação: Idade vs Uso',
            color_continuous_scale='YlOrRd'
        )
        st.plotly_chart(fig_heatmap, use_container_width=True)
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Clientes de alto valor
            st.subheader("💎 Clientes de Alto Valor")
            limite_alto = df_filtrado['Limite'].quantile(0.75)
            clientes_alto_valor = df_filtrado[df_filtrado['Limite'] > limite_alto]
            
            st.metric("Quantidade", f"{len(clientes_alto_valor):,}")
            st.metric("Limite Médio", f"R$ {clientes_alto_valor['Limite'].mean():,.0f}")
            st.metric("Valor Médio Transações", f"R$ {clientes_alto_valor['Valor Transacoes 12m'].mean():,.0f}")
            
            # Distribuição por categoria
            fig_alto_valor = px.pie(
                clientes_alto_valor,
                names='Categoria Cartão',
                title='Distribuição de Categorias (Alto Valor)',
                hole=0.4
            )
            st.plotly_chart(fig_alto_valor, use_container_width=True)
        
        with col2:
            # Clientes em risco
            st.subheader("⚠️ Clientes em Risco")
            clientes_risco = df_filtrado[df_filtrado['Inatividade 12m'] >= 3]
            
            st.metric("Quantidade", f"{len(clientes_risco):,}")
            st.metric("% do Total", f"{len(clientes_risco)/len(df_filtrado)*100:.1f}%")
            st.metric("Taxa Utilização Média", f"{clientes_risco['Taxa de Utilização Cartão'].mean():.1%}")
            
            # Produtos contratados por clientes em risco
            fig_risco = px.bar(
                clientes_risco['Produtos Contratados'].value_counts().sort_index().reset_index(),
                x='Produtos Contratados',
                y='count',
                title='Produtos dos Clientes em Risco',
                color='count',
                color_continuous_scale='reds'
            )
            st.plotly_chart(fig_risco, use_container_width=True)
        
        # Insights principais
        st.markdown("---")
        st.subheader("💡 Insights Principais")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.info(f"""
            **👤 Perfil Típico**
            - Idade média: {df_filtrado['Idade'].mean():.0f} anos
            - Sexo predominante: {df_filtrado['Sexo'].mode()[0]}
            - Cartão mais comum: {df_filtrado['Categoria Cartão'].mode()[0]}
            - Produtos em média: {df_filtrado['Produtos Contratados'].mean():.1f}
            """)
        
        with col2:
            clientes_poucos_produtos = df_filtrado[df_filtrado['Produtos Contratados'] <= 2]
            st.warning(f"""
            **🎯 Oportunidades Cross-sell**
            - Clientes com ≤2 produtos: {len(clientes_poucos_produtos):,}
            - Representa: {len(clientes_poucos_produtos)/len(df_filtrado)*100:.1f}%
            - Limite médio: R$ {clientes_poucos_produtos['Limite'].mean():,.0f}
            - Potencial de expansão
            """)
        
        with col3:
            utilizacao_baixa = df_filtrado[df_filtrado['Taxa de Utilização Cartão'] < 0.3]
            st.success(f"""
            **📈 Potencial de Crescimento**
            - Taxa utilização < 30%: {len(utilizacao_baixa):,}
            - Limite disponível médio: R$ {utilizacao_baixa['Limite Disponível'].mean():,.0f}
            - Oportunidade para campanhas
            """)
        
        # Correlações
        st.markdown("---")
        st.subheader("🔗 Análise de Correlações")
        
        colunas_correlacao = [
            'Idade', 'Dependentes', 'Meses como Cliente', 'Produtos Contratados',
            'Limite', 'Taxa de Utilização Cartão', 'Valor Transacoes 12m',
            'Qtde Transacoes 12m', 'Inatividade 12m', 'Contatos 12m'
        ]
        
        correlacao = df_filtrado[colunas_correlacao].corr()
        
        fig_corr = px.imshow(
            correlacao,
            text_auto='.2f',
            aspect='auto',
            color_continuous_scale='RdBu_r',
            title='Matriz de Correlação'
        )
        st.plotly_chart(fig_corr, use_container_width=True)


if __name__ == "__main__":
    main()
