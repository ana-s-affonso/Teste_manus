from dash import html
import dash_bootstrap_components as dbc
import plotly.express as px

# Exemplo de dados para o gráfico
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                 title="Largura vs Comprimento da Sépala (Iris)")

# Layout da Página 1
layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Página 1", className="text-center text-primary mb-4"), width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.P("Este é o conteúdo da primeira página do dashboard."),
            html.P("Abaixo, um exemplo de gráfico interativo usando Plotly Express:"),
            dbc.Graph(figure=fig)
        ], width=12)
    ])
], fluid=True)

