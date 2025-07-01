import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, dcc, html

# 1. Carregar o arquivo
df = pd.read_csv('ecommerce_estatistica.csv')

def cria_graficos(df):

    # Histograma de Preço
    fig_hist = px.histogram(df, x='Preço', nbins=30, title='Distribuição de Preços', color_discrete_sequence=['orange'])

    # Dispersão Preço vs Nota
    fig_disp = px.scatter(df, x='Preço', y='Nota', title='Preço vs Nota', color_discrete_sequence=['purple'])

    # Heatmap de Correlação
    df_corr = df[['Nota', 'N_Avaliações', 'Desconto', 'Preço']].corr()
    fig_heat = go.Figure(data=go.Heatmap(
        z=df_corr.values,
        x=df_corr.columns,
        y=df_corr.index,
        colorscale='RdBu',
        zmin=-1, zmax=1,
        colorbar=dict(title="Correlação")
    ))
    fig_heat.update_layout(title='Mapa de Calor da Correlação')

    # Gráfico de Barra - Notas por Marca
    top_marcas = df['Marca'].value_counts().nlargest(10).index
    df_top = df[df['Marca'].isin(top_marcas)]
    fig_bar = px.bar(df_top, x='Marca', y='Nota', title='Nota Média das 10 Marcas com Mais Produtos',
                     color_discrete_sequence=['steelblue'])
    fig_bar.update_layout(xaxis={'categoryorder': 'total descending'})

    # Gráfico de Pizza - Participação das Marcas
    contagem_marcas = df_top['Marca'].value_counts()
    fig_pie = px.pie(values=contagem_marcas.values, names=contagem_marcas.index,
                     title='Participação das 10 Marcas com Mais Produtos')

    # Gráfico de Densidade - Nota
    fig_kde = px.histogram(df, x='Nota', marginal='rug', histnorm='density',
                           title='Distribuição de Densidade da Nota',
                           color_discrete_sequence=['skyblue'])

    # Gráfico de Regressão - Preço vs Nota
    fig_reg = px.scatter(df, x='Preço', y='Nota', trendline='ols',
                         title='Regressão Linear: Preço vs Nota')

    return fig_hist, fig_disp, fig_heat, fig_bar, fig_pie, fig_kde, fig_reg



# 4. Layout da aplicação
def cria_app(df):
    app = Dash(__name__)

    fig_hist, fig_disp, fig_heat, fig_bar, fig_pie, fig_kde, fig_reg = cria_graficos(df)

    app.title = "Dashboard E-commerce"
    app.layout = html.Div([
        html.H1("📊 Dashboard de Produtos de E-commerce", style={'textAlign': 'center'}),

        dcc.Graph(figure=fig_hist),
        dcc.Graph(figure=fig_disp),
        dcc.Graph(figure=fig_heat),
        dcc.Graph(figure=fig_bar),
        dcc.Graph(figure=fig_pie),
        dcc.Graph(figure=fig_kde),
        dcc.Graph(figure=fig_reg),

        html.P("Desenvolvido com Dash e Plotly", style={'textAlign': 'center', 'marginTop': '30px', 'color': 'gray'})
    ])
    return app

# 5. Rodar a aplicação
if __name__ == '__main__':
    app = cria_app(df)
    # Executa App
    app.run(debug=True, port=8050)