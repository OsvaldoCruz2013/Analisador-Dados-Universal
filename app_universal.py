"""
Dashboard Streamlit - Analisador Universal de Dados CSV
Aplicação genérica para análise de QUALQUER arquivo CSV
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import io
import warnings
warnings.filterwarnings('ignore')

# Configuração da página
st.set_page_config(
    page_title="Analisador Universal de Dados CSV",
    page_icon="📊",
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
    .sub-header {
        font-size: 1.5rem;
        color: #ff7f0e;
        margin-top: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

@st.cache_data
def carregar_dados(arquivo_bytes=None, caminho=None):
    """Carrega dados de arquivo CSV"""
    try:
        if arquivo_bytes is not None:
            # Usar BytesIO para criar um novo objeto de arquivo a partir dos bytes
            df = pd.read_csv(io.BytesIO(arquivo_bytes), encoding='utf-8')
        elif caminho:
            df = pd.read_csv(caminho, encoding='utf-8')
        else:
            return None
    except UnicodeDecodeError:
        if arquivo_bytes is not None:
            # Tentar novamente com encoding latin-1
            df = pd.read_csv(io.BytesIO(arquivo_bytes), encoding='latin-1')
        else:
            df = pd.read_csv(caminho, encoding='latin-1')
    
    return df

def detectar_tipos_colunas(df):
    """Detecta automaticamente os tipos de dados das colunas"""
    tipos = {
        'numericas': [],
        'categoricas': [],
        'datas': [],
        'booleanas': [],
        'textos': []
    }
    
    for col in df.columns:
        # Pular colunas com muitos valores nulos
        if df[col].isnull().sum() / len(df) > 0.9:
            continue
            
        # Verificar se é datetime
        if pd.api.types.is_datetime64_any_dtype(df[col]):
            tipos['datas'].append(col)
        # Verificar se é numérico
        elif pd.api.types.is_numeric_dtype(df[col]):
            tipos['numericas'].append(col)
        # Verificar se é booleano
        elif pd.api.types.is_bool_dtype(df[col]) or df[col].nunique() == 2:
            tipos['booleanas'].append(col)
        # Verificar se é categórico (menos de 20 valores únicos)
        elif df[col].nunique() < 20:
            tipos['categoricas'].append(col)
        # Tentar converter para data
        elif df[col].dtype == 'object':
            try:
                pd.to_datetime(df[col], errors='raise')
                tipos['datas'].append(col)
            except:
                # Se tem muitos valores únicos, é texto
                if df[col].nunique() > 50:
                    tipos['textos'].append(col)
                else:
                    tipos['categoricas'].append(col)
    
    return tipos

def analise_basica(df):
    """Exibe análise básica do dataset"""
    st.header("📊 Visão Geral dos Dados")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total de Registros", f"{len(df):,}")
    
    with col2:
        st.metric("Total de Colunas", len(df.columns))
    
    with col3:
        percent_completo = (1 - df.isnull().sum().sum() / (len(df) * len(df.columns))) * 100
        st.metric("Completude", f"{percent_completo:.1f}%")
    
    with col4:
        memoria = df.memory_usage(deep=True).sum() / 1024**2
        st.metric("Tamanho em Memória", f"{memoria:.2f} MB")
    
    st.markdown("---")
    
    # Informações das colunas
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📋 Colunas Disponíveis")
        col_info = pd.DataFrame({
            'Coluna': df.columns,
            'Tipo': df.dtypes.astype(str),
            'Não-Nulos': df.count(),
            'Nulos': df.isnull().sum(),
            '% Nulos': (df.isnull().sum() / len(df) * 100).round(2)
        })
        st.dataframe(col_info, use_container_width=True, height=300)
    
    with col2:
        st.subheader("📈 Valores Únicos por Coluna")
        unique_counts = pd.DataFrame({
            'Coluna': df.columns,
            'Valores Únicos': [df[col].nunique() for col in df.columns],
            '% Únicos': [round(df[col].nunique() / len(df) * 100, 2) for col in df.columns]
        }).sort_values('Valores Únicos', ascending=False)
        st.dataframe(unique_counts, use_container_width=True, height=300)
    
    # Amostra dos dados
    st.subheader("🔍 Amostra dos Dados")
    st.dataframe(df.head(100), use_container_width=True, height=300)

def analise_numerica(df, colunas_numericas):
    """Análise de variáveis numéricas"""
    st.header("🔢 Análise de Variáveis Numéricas")
    
    if not colunas_numericas:
        st.warning("⚠️ Nenhuma coluna numérica encontrada no dataset.")
        return
    
    # Estatísticas descritivas
    st.subheader("📊 Estatísticas Descritivas")
    st.dataframe(df[colunas_numericas].describe(), use_container_width=True)
    
    st.markdown("---")
    
    # Seletor de coluna
    st.subheader("📈 Distribuições")
    col_selecionada = st.selectbox(
        "Selecione a coluna numérica para análise:",
        colunas_numericas,
        key="num_col_select"
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Histograma
        fig_hist = px.histogram(
            df,
            x=col_selecionada,
            title=f'Distribuição de {col_selecionada}',
            nbins=50,
            color_discrete_sequence=['#1f77b4']
        )
        st.plotly_chart(fig_hist, use_container_width=True)
    
    with col2:
        # Box plot
        fig_box = px.box(
            df,
            y=col_selecionada,
            title=f'Box Plot de {col_selecionada}',
            color_discrete_sequence=['#2ca02c']
        )
        st.plotly_chart(fig_box, use_container_width=True)
    
    # Correlação se houver múltiplas colunas numéricas
    if len(colunas_numericas) > 1:
        st.markdown("---")
        st.subheader("🔗 Matriz de Correlação")
        
        correlacao = df[colunas_numericas].corr()
        
        fig_corr = px.imshow(
            correlacao,
            text_auto='.2f',
            aspect='auto',
            color_continuous_scale='RdBu_r',
            title='Correlação entre Variáveis Numéricas'
        )
        st.plotly_chart(fig_corr, use_container_width=True)

def analise_categorica(df, colunas_categoricas):
    """Análise de variáveis categóricas"""
    st.header("📊 Análise de Variáveis Categóricas")
    
    if not colunas_categoricas:
        st.warning("⚠️ Nenhuma coluna categórica encontrada no dataset.")
        return
    
    # Seletor de coluna
    col_selecionada = st.selectbox(
        "Selecione a coluna categórica para análise:",
        colunas_categoricas,
        key="cat_col_select"
    )
    
    # Distribuição de valores
    valor_counts = df[col_selecionada].value_counts()
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Gráfico de barras
        fig_bar = px.bar(
            x=valor_counts.index,
            y=valor_counts.values,
            title=f'Distribuição de {col_selecionada}',
            labels={'x': col_selecionada, 'y': 'Quantidade'},
            color=valor_counts.values,
            color_continuous_scale='viridis'
        )
        st.plotly_chart(fig_bar, use_container_width=True)
    
    with col2:
        # Gráfico de pizza
        fig_pie = px.pie(
            values=valor_counts.values,
            names=valor_counts.index,
            title=f'Proporção de {col_selecionada}',
            hole=0.4
        )
        st.plotly_chart(fig_pie, use_container_width=True)
    
    # Tabela de frequências
    st.subheader("📋 Tabela de Frequências")
    freq_df = pd.DataFrame({
        'Categoria': valor_counts.index,
        'Quantidade': valor_counts.values,
        'Percentual': [round(v / len(df) * 100, 2) for v in valor_counts.values]
    })
    st.dataframe(freq_df, use_container_width=True)

def analise_cruzada(df, tipos):
    """Análise cruzada entre variáveis"""
    st.header("🔄 Análise Cruzada")
    
    colunas_numericas = tipos['numericas']
    colunas_categoricas = tipos['categoricas']
    
    if not colunas_numericas or not colunas_categoricas:
        st.warning("⚠️ É necessário ter pelo menos uma coluna numérica e uma categórica para análise cruzada.")
        return
    
    col1, col2 = st.columns(2)
    
    with col1:
        col_numerica = st.selectbox(
            "Selecione a coluna numérica:",
            colunas_numericas,
            key="cross_num"
        )
    
    with col2:
        col_categorica = st.selectbox(
            "Selecione a coluna categórica:",
            colunas_categoricas,
            key="cross_cat"
        )
    
    # Box plot por categoria
    fig_box = px.box(
        df,
        x=col_categorica,
        y=col_numerica,
        color=col_categorica,
        title=f'{col_numerica} por {col_categorica}'
    )
    st.plotly_chart(fig_box, use_container_width=True)
    
    # Estatísticas por grupo
    st.subheader("📊 Estatísticas por Grupo")
    stats_grupo = df.groupby(col_categorica)[col_numerica].agg([
        'count', 'mean', 'median', 'std', 'min', 'max'
    ]).round(2)
    st.dataframe(stats_grupo, use_container_width=True)

def analise_temporal(df, colunas_datas, tipos):
    """Análise de séries temporais"""
    st.header("📅 Análise Temporal")
    
    if not colunas_datas:
        st.warning("⚠️ Nenhuma coluna de data encontrada no dataset.")
        return
    
    col_data = st.selectbox(
        "Selecione a coluna de data:",
        colunas_datas,
        key="date_col"
    )
    
    # Converter para datetime se necessário
    if not pd.api.types.is_datetime64_any_dtype(df[col_data]):
        df[col_data] = pd.to_datetime(df[col_data])
    
    # Ordenar por data
    df_temporal = df.sort_values(col_data)
    
    # Contagem ao longo do tempo
    fig_timeline = px.histogram(
        df_temporal,
        x=col_data,
        title=f'Distribuição ao Longo do Tempo',
        nbins=50
    )
    st.plotly_chart(fig_timeline, use_container_width=True)
    
    # Se houver colunas numéricas, permitir análise temporal
    if tipos['numericas']:
        col_metrica = st.selectbox(
            "Selecione uma métrica para análise temporal:",
            tipos['numericas'],
            key="temporal_metric"
        )
        
        # Agregação por período
        periodo = st.radio(
            "Selecione o período de agregação:",
            ["Dia", "Semana", "Mês", "Ano"],
            horizontal=True
        )
        
        freq_map = {"Dia": "D", "Semana": "W", "Mês": "M", "Ano": "Y"}
        
        df_temporal_agg = df_temporal.set_index(col_data)[col_metrica].resample(
            freq_map[periodo]
        ).agg(['mean', 'sum', 'count'])
        
        fig_temporal = go.Figure()
        fig_temporal.add_trace(go.Scatter(
            x=df_temporal_agg.index,
            y=df_temporal_agg['mean'],
            name='Média',
            mode='lines+markers'
        ))
        fig_temporal.update_layout(
            title=f'{col_metrica} - Média por {periodo}',
            xaxis_title='Data',
            yaxis_title=col_metrica
        )
        st.plotly_chart(fig_temporal, use_container_width=True)

def insights_automaticos(df, tipos):
    """Gera insights automáticos sobre os dados"""
    st.header("💡 Insights Automáticos")
    
    insights = []
    
    # Colunas com muitos nulos
    colunas_nulos = df.columns[df.isnull().sum() > len(df) * 0.5]
    if len(colunas_nulos) > 0:
        insights.append(f"⚠️ **Atenção**: {len(colunas_nulos)} coluna(s) com mais de 50% de valores nulos: {', '.join(colunas_nulos[:3])}")
    
    # Colunas com valores únicos (possíveis IDs)
    for col in df.columns:
        if df[col].nunique() == len(df):
            insights.append(f"🔑 **{col}**: Possui valores únicos - possível identificador único")
    
    # Variáveis numéricas com outliers
    for col in tipos['numericas'][:5]:  # Limitar a 5 colunas
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        outliers = ((df[col] < (Q1 - 1.5 * IQR)) | (df[col] > (Q3 + 1.5 * IQR))).sum()
        if outliers > 0:
            insights.append(f"📊 **{col}**: Detectados {outliers} outliers ({outliers/len(df)*100:.1f}%)")
    
    # Variáveis categóricas desbalanceadas
    for col in tipos['categoricas'][:5]:
        valor_counts = df[col].value_counts()
        if len(valor_counts) > 1:
            proporcao_maior = valor_counts.iloc[0] / len(df)
            if proporcao_maior > 0.8:
                insights.append(f"⚖️ **{col}**: Desbalanceada - {valor_counts.index[0]} representa {proporcao_maior*100:.1f}% dos dados")
    
    # Correlações fortes
    if len(tipos['numericas']) > 1:
        correlacao = df[tipos['numericas']].corr()
        for i in range(len(correlacao.columns)):
            for j in range(i+1, len(correlacao.columns)):
                if abs(correlacao.iloc[i, j]) > 0.7:
                    insights.append(f"🔗 **Correlação forte** ({correlacao.iloc[i, j]:.2f}) entre {correlacao.columns[i]} e {correlacao.columns[j]}")
    
    # Exibir insights
    if insights:
        for insight in insights[:10]:  # Limitar a 10 insights
            st.markdown(insight)
    else:
        st.info("✅ Nenhum insight crítico detectado. Os dados parecem estar em boa forma!")

def main():
    """Função principal do dashboard"""
    
    # Cabeçalho
    st.markdown('<h1 class="main-header">📊 Analisador Universal de Dados CSV</h1>', unsafe_allow_html=True)
    st.markdown("**Faça upload de qualquer arquivo CSV e obtenha análises automáticas instantâneas!**")
    st.markdown("---")
    
    # Sidebar
    st.sidebar.title("⚙️ Configurações")
    st.sidebar.markdown("---")
    
    # Upload de arquivo
    st.sidebar.markdown("### 📂 Carregar Dados")
    arquivo_upload = st.sidebar.file_uploader(
        "Selecione seu arquivo CSV",
        type=['csv'],
        help="Faça upload de qualquer arquivo CSV para análise automática"
    )
    
    if arquivo_upload is None:
        # Tela de boas-vindas
        st.info("👆 **Comece fazendo upload de um arquivo CSV na barra lateral**")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            ### 📊 Análises Automáticas
            - Detecção automática de tipos de dados
            - Estatísticas descritivas
            - Identificação de outliers
            - Correlações
            """)
        
        with col2:
            st.markdown("""
            ### 📈 Visualizações
            - Gráficos interativos
            - Distribuições
            - Séries temporais
            - Análises cruzadas
            """)
        
        with col3:
            st.markdown("""
            ### 💡 Insights
            - Detecção de problemas
            - Sugestões de limpeza
            - Padrões nos dados
            - Recomendações
            """)
        
        st.markdown("---")
        st.markdown("""
        ### 📋 Formatos Suportados
        - CSV com separador vírgula (,)
        - CSV com separador ponto-e-vírgula (;)
        - Encoding UTF-8 ou Latin-1
        - Qualquer estrutura de colunas
        """)
        
        st.stop()
    
    # Carregar dados
    try:
        # Ler o conteúdo do arquivo como bytes para evitar erro "I/O operation on closed file"
        arquivo_bytes = arquivo_upload.read()
        df = carregar_dados(arquivo_bytes=arquivo_bytes)
        st.sidebar.success(f"✅ {len(df):,} registros carregados")
        st.sidebar.markdown(f"**Colunas:** {len(df.columns)}")
    except Exception as e:
        st.error(f"❌ Erro ao carregar arquivo: {e}")
        st.stop()
    
    # Detectar tipos de colunas
    tipos = detectar_tipos_colunas(df)
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📊 Tipos Detectados")
    st.sidebar.markdown(f"🔢 Numéricas: {len(tipos['numericas'])}")
    st.sidebar.markdown(f"📊 Categóricas: {len(tipos['categoricas'])}")
    st.sidebar.markdown(f"📅 Datas: {len(tipos['datas'])}")
    st.sidebar.markdown(f"✓ Booleanas: {len(tipos['booleanas'])}")
    
    # Filtros
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 🔍 Filtros")
    
    # Permitir filtros apenas se houver colunas categóricas
    df_filtrado = df.copy()
    
    if tipos['categoricas']:
        col_filtro = st.sidebar.selectbox(
            "Filtrar por:",
            ["Nenhum"] + tipos['categoricas']
        )
        
        if col_filtro != "Nenhum":
            valores_unicos = df[col_filtro].unique()
            valores_selecionados = st.sidebar.multiselect(
                f"Selecione valores de {col_filtro}:",
                valores_unicos,
                default=list(valores_unicos)
            )
            df_filtrado = df_filtrado[df_filtrado[col_filtro].isin(valores_selecionados)]
            st.sidebar.markdown(f"**Registros após filtro:** {len(df_filtrado):,}")
    
    # Tabs de análise
    tabs = st.tabs([
        "📊 Visão Geral",
        "🔢 Variáveis Numéricas",
        "📊 Variáveis Categóricas",
        "🔄 Análise Cruzada",
        "📅 Análise Temporal",
        "💡 Insights"
    ])
    
    with tabs[0]:
        analise_basica(df_filtrado)
    
    with tabs[1]:
        analise_numerica(df_filtrado, tipos['numericas'])
    
    with tabs[2]:
        analise_categorica(df_filtrado, tipos['categoricas'])
    
    with tabs[3]:
        analise_cruzada(df_filtrado, tipos)
    
    with tabs[4]:
        analise_temporal(df_filtrado, tipos['datas'], tipos)
    
    with tabs[5]:
        insights_automaticos(df_filtrado, tipos)


# Executar o dashboard
main()
