# 📊 Análise Exploratória de Dados de E-commerce

Este projeto tem como objetivo realizar uma **análise exploratória de dados (EDA)** em um conjunto de dados de e-commerce utilizando **Python**, com foco em entender a relação entre variáveis como preço, nota, número de avaliações, desconto e marca.

As análises são feitas por meio de gráficos estatísticos com o uso das bibliotecas **Pandas**, **Seaborn** e **Matplotlib**.

## 🔧 Tecnologias Utilizadas

- Python 3.x
- Pandas
- Matplotlib
- Seaborn
- Plotly
- Dash

## 📁 Sobre os Dados

O dataset `ecommerce_estatistica.csv` contém informações sobre produtos de uma loja virtual, incluindo:

- `Preço`: valor do produto  
- `Nota`: avaliação média dos consumidores  
- `N_Avaliações`: número total de avaliações  
- `Desconto`: percentual de desconto aplicado  
- `Marca`: marca do produto  

## 📊 Etapas da Análise

1. **Carregamento e inspeção inicial do dataset**
   - Visualização das primeiras linhas
   - Verificação de dimensões, colunas, tipos de dados e valores ausentes
   - Estatísticas descritivas

2. **Visualizações e Gráficos**
   - **Histograma**: distribuição de preços dos produtos  
   - **Gráfico de dispersão**: relação entre preço e nota  
   - **Mapa de calor (Heatmap)**: correlação entre variáveis numéricas  
   - **Gráfico de barras**: nota média das 10 marcas com mais produtos  
   - **Gráfico de pizza**: participação das principais marcas  
   - **Gráfico de densidade**: distribuição da nota média  
   - **Gráfico de regressão**: tendência entre preço e nota  

## 📂 Projeto Interativo com Dash

Além dos gráficos estáticos, o projeto também conta com um arquivo chamado **`projeto_graficos_interativos.py`**, que gera os **mesmos gráficos de forma interativa** utilizando **Plotly** e **Dash**.  

A aplicação web pode ser acessada localmente pelo seguinte endereço:  
🔗 [http://127.0.0.1:8050/](http://127.0.0.1:8050/)

Isso permite que qualquer usuário visualize os dados sem precisar usar Python diretamente.

## 📌 Objetivos

- Explorar os dados de maneira visual e estatística  
- Identificar padrões, tendências e correlações  
- Praticar habilidades de análise e visualização com Python  
- Apresentar os resultados de forma interativa para facilitar a interpretação

## 🚀 Como Executar

1. Clone o repositório
2. Instale as dependências com:
   ```bash
   pip install pandas matplotlib seaborn plotly dash
