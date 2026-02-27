"""
Análise de Dados - ClientesBanco.csv
Script para análise exploratória de dados de clientes bancários
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import sys
import io

# Configurar encoding do console para UTF-8 (somente Windows)
try:
    # Tentar configurar encoding apenas se estiver em ambiente local (Windows)
    if hasattr(sys.stdout, 'buffer'):
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
except (AttributeError, ValueError):
    # No Streamlit Cloud ou ambientes sem buffer, ignorar
    pass

# Configurar estilo dos gráficos
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

class AnaliseBancoDados:
    """Classe para análise de dados de clientes do banco"""
    
    def __init__(self, caminho_arquivo):
        """Inicializa a análise carregando os dados"""
        self.df = pd.read_csv(caminho_arquivo, encoding='latin-1')
        self.caminho_arquivo = caminho_arquivo
        print(f"[OK] Dados carregados: {len(self.df)} registros")
        
    def informacoes_basicas(self):
        """Retorna informações básicas sobre o dataset"""
        print("\n" + "="*70)
        print("INFORMAÇÕES BÁSICAS DO DATASET")
        print("="*70)
        
        print(f"\n[DADOS] Dimensões: {self.df.shape[0]} linhas x {self.df.shape[1]} colunas")
        print(f"\n[LISTA] Colunas disponíveis:")
        for i, col in enumerate(self.df.columns, 1):
            print(f"  {i:2d}. {col}")
        
        print(f"\n[INFO] Tipos de dados:")
        print(self.df.dtypes)
        
        print(f"\n[NULOS] Valores nulos:")
        nulos = self.df.isnull().sum()
        if nulos.sum() > 0:
            print(nulos[nulos > 0])
        else:
            print("  Nenhum valor nulo encontrado!")
        
        print(f"\n[STATS] Estatísticas descritivas:")
        print(self.df.describe())
        
        return self.df.info()
    
    def analise_demografica(self):
        """Análise demográfica dos clientes"""
        print("\n" + "="*70)
        print("ANÁLISE DEMOGRÁFICA")
        print("="*70)
        
        # Distribuição por sexo
        print("\n[SEXO] Distribuição por Sexo:")
        sexo_dist = self.df['Sexo'].value_counts()
        print(sexo_dist)
        print(f"  Percentual: {(sexo_dist / len(self.df) * 100).round(2)}%")
        
        # Estatísticas de idade
        print("\n[IDADE] Estatísticas de Idade:")
        print(f"  Idade média: {self.df['Idade'].mean():.1f} anos")
        print(f"  Idade mediana: {self.df['Idade'].median():.1f} anos")
        print(f"  Idade mínima: {self.df['Idade'].min()} anos")
        print(f"  Idade máxima: {self.df['Idade'].max()} anos")
        
        # Distribuição por estado civil
        print("\n[ESTADO CIVIL] Estado Civil:")
        print(self.df['Estado Civil'].value_counts())
        
        # Distribuição por educação
        print("\n[EDUCACAO] Nível de Educação:")
        print(self.df['Educação'].value_counts())
        
        # Dependentes
        print("\n[DEPENDENTES] Dependentes:")
        print(self.df['Dependentes'].value_counts().sort_index())
        
    def analise_financeira(self):
        """Análise financeira dos clientes"""
        print("\n" + "="*70)
        print("ANÁLISE FINANCEIRA")
        print("="*70)
        
        # Faixa salarial
        print("\n[SALARIO] Distribuição por Faixa Salarial:")
        print(self.df['Faixa Salarial Anual'].value_counts())
        
        # Categoria de cartão
        print("\n[CARTAO] Categoria de Cartão:")
        cartao_dist = self.df['Categoria Cartão'].value_counts()
        print(cartao_dist)
        
        # Estatísticas de limite
        print("\n[LIMITE] Estatísticas de Limite de Crédito:")
        print(f"  Limite médio: R$ {self.df['Limite'].mean():,.2f}")
        print(f"  Limite mediano: R$ {self.df['Limite'].median():,.2f}")
        print(f"  Limite mínimo: R$ {self.df['Limite'].min():,.2f}")
        print(f"  Limite máximo: R$ {self.df['Limite'].max():,.2f}")
        
        # Taxa de utilização
        print("\n[DADOS] Taxa de Utilização do Cartão:")
        print(f"  Média: {self.df['Taxa de Utilização Cartão'].mean():.2%}")
        print(f"  Mediana: {self.df['Taxa de Utilização Cartão'].median():.2%}")
        
        # Valor de transações
        print("\n[TRANSACOES] Valor de Transações (12 meses):")
        print(f"  Média: R$ {self.df['Valor Transacoes 12m'].mean():,.2f}")
        print(f"  Mediana: R$ {self.df['Valor Transacoes 12m'].median():,.2f}")
        print(f"  Total: R$ {self.df['Valor Transacoes 12m'].sum():,.2f}")
        
    def analise_comportamento(self):
        """Análise de comportamento dos clientes"""
        print("\n" + "="*70)
        print("ANÁLISE DE COMPORTAMENTO")
        print("="*70)
        
        # Tempo como cliente
        print("\n[TEMPO] Tempo como Cliente:")
        print(f"  Média: {self.df['Meses como Cliente'].mean():.1f} meses")
        print(f"  Mediana: {self.df['Meses como Cliente'].median():.1f} meses")
        
        # Produtos contratados
        print("\n[PRODUTOS] Produtos Contratados:")
        print(self.df['Produtos Contratados'].value_counts().sort_index())
        print(f"  Média de produtos por cliente: {self.df['Produtos Contratados'].mean():.2f}")
        
        # Inatividade
        print("\n[INATIVIDADE] Meses de Inatividade (últimos 12 meses):")
        print(self.df['Inatividade 12m'].value_counts().sort_index())
        print(f"  Média: {self.df['Inatividade 12m'].mean():.2f} meses")
        
        # Contatos
        print("\n[CONTATOS] Contatos (últimos 12 meses):")
        print(self.df['Contatos 12m'].value_counts().sort_index())
        print(f"  Média: {self.df['Contatos 12m'].mean():.2f} contatos")
        
        # Quantidade de transações
        print("\n[QTD TRANSACOES] Quantidade de Transações (12 meses):")
        print(f"  Média: {self.df['Qtde Transacoes 12m'].mean():.1f} transações")
        print(f"  Mediana: {self.df['Qtde Transacoes 12m'].median():.1f} transações")
        
    def correlacoes(self):
        """Análise de correlações entre variáveis numéricas"""
        print("\n" + "="*70)
        print("ANÁLISE DE CORRELAÇÕES")
        print("="*70)
        
        # Selecionar apenas colunas numéricas
        colunas_numericas = self.df.select_dtypes(include=[np.number]).columns
        correlacao = self.df[colunas_numericas].corr()
        
        # Mostrar correlações mais fortes com Taxa de Utilização
        if 'Taxa de Utilização Cartão' in correlacao.columns:
            print("\n[CORRELACAO] Correlações com Taxa de Utilização do Cartão:")
            corr_utilizacao = correlacao['Taxa de Utilização Cartão'].sort_values(ascending=False)
            print(corr_utilizacao)
        
        return correlacao
    
    def segmentacao_clientes(self):
        """Segmentação de clientes por características"""
        print("\n" + "="*70)
        print("SEGMENTAÇÃO DE CLIENTES")
        print("="*70)
        
        # Criar segmentos por idade
        self.df['Segmento_Idade'] = pd.cut(
            self.df['Idade'], 
            bins=[0, 30, 40, 50, 100], 
            labels=['Jovem', 'Adulto', 'Meia-idade', 'Sênior']
        )
        
        # Criar segmentos por uso do cartão
        self.df['Segmento_Uso'] = pd.cut(
            self.df['Taxa de Utilização Cartão'],
            bins=[-0.01, 0.3, 0.6, 1.0],
            labels=['Baixo Uso', 'Uso Moderado', 'Alto Uso']
        )
        
        print("\n[SEGMENTACAO] Segmentação por Idade e Uso do Cartão:")
        segmentacao = pd.crosstab(
            self.df['Segmento_Idade'], 
            self.df['Segmento_Uso'],
            margins=True
        )
        print(segmentacao)
        
        return segmentacao
    
    def insights_principais(self):
        """Gera insights principais dos dados"""
        print("\n" + "="*70)
        print("[INSIGHTS] INSIGHTS PRINCIPAIS")
        print("="*70)
        
        # Perfil do cliente típico
        idade_media = self.df['Idade'].mean()
        sexo_predominante = self.df['Sexo'].mode()[0]
        cartao_mais_comum = self.df['Categoria Cartão'].mode()[0]
        produtos_media = self.df['Produtos Contratados'].mean()
        
        print(f"\n[PERFIL] Perfil do Cliente Típico:")
        print(f"  • Idade média: {idade_media:.0f} anos")
        print(f"  • Sexo predominante: {sexo_predominante}")
        print(f"  • Categoria de cartão mais comum: {cartao_mais_comum}")
        print(f"  • Produtos contratados em média: {produtos_media:.1f}")
        
        # Clientes de alto valor
        limite_alto = self.df['Limite'].quantile(0.75)
        clientes_alto_valor = self.df[self.df['Limite'] > limite_alto]
        print(f"\n[ALTO VALOR] Clientes de Alto Valor (top 25%):")
        print(f"  • Quantidade: {len(clientes_alto_valor)}")
        print(f"  • Limite médio: R$ {clientes_alto_valor['Limite'].mean():,.2f}")
        print(f"  • Valor médio de transações: R$ {clientes_alto_valor['Valor Transacoes 12m'].mean():,.2f}")
        
        # Clientes em risco (alta inatividade)
        clientes_risco = self.df[self.df['Inatividade 12m'] >= 3]
        print(f"\n[RISCO] Clientes em Risco (3+ meses inativos):")
        print(f"  • Quantidade: {len(clientes_risco)} ({len(clientes_risco)/len(self.df)*100:.1f}%)")
        print(f"  • Taxa média de utilização: {clientes_risco['Taxa de Utilização Cartão'].mean():.2%}")
        
        # Oportunidades de cross-sell
        clientes_poucos_produtos = self.df[self.df['Produtos Contratados'] <= 2]
        print(f"\n[SEGMENTACAO] Oportunidades de Cross-sell (≤2 produtos):")
        print(f"  • Quantidade: {len(clientes_poucos_produtos)} ({len(clientes_poucos_produtos)/len(self.df)*100:.1f}%)")
        print(f"  • Limite médio: R$ {clientes_poucos_produtos['Limite'].mean():,.2f}")


def main():
    """Função principal"""
    # Buscar arquivo ClientesBanco.csv em locais padrão
    caminhos_possiveis = [
        Path("ClientesBanco.csv"),
        Path("data/ClientesBanco.csv"),
        Path("data") / "ClientesBanco.csv",
        Path("..") / "ClientesBanco.csv"
    ]
    
    caminho = None
    for caminho_teste in caminhos_possiveis:
        if caminho_teste.exists():
            caminho = str(caminho_teste)
            print(f"[OK] Arquivo encontrado: {caminho}")
            break
    
    if not caminho:
        print("[ERRO] Arquivo ClientesBanco.csv não encontrado!")
        print("Coloque o arquivo na raiz do projeto ou na pasta data/")
        sys.exit(1)
    
    # Criar instância da análise
    analise = AnaliseBancoDados(caminho)
    
    # Executar todas as análises
    analise.informacoes_basicas()
    analise.analise_demografica()
    analise.analise_financeira()
    analise.analise_comportamento()
    analise.correlacoes()
    analise.segmentacao_clientes()
    analise.insights_principais()
    
    print("\n" + "="*70)
    print("[OK] Análise concluída!")
    print("="*70)


if __name__ == "__main__":
    main()
