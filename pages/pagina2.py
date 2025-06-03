from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.graph_objects as go

# Exemplo de dados para outro gráfico
fig = go.Figure(data=[go.Bar(y=[2, 1, 3])])
fig.update_layout(title_text="Exemplo de Gráfico de Barras")

# Layout da Página 2
layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Página 2", className="text-center text-success mb-4"), width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.P("Este é o conteúdo da segunda página."),
            html.P("Aqui podemos ter outras visualizações ou informações."),
            dcc.Graph(figure=fig)
        ], width=12)
    ])
], fluid=True)

