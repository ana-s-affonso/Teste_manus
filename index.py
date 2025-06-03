from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

# Importa a instância da app e o server (necessário para deploy)
from app import app, server
# Importa os layouts das páginas e componentesrom pages import pagina1, pagina2
from components import navbar

# Define o layout principal da aplicação
app.layout = html.Div([
    dcc.Location(id='url', refresh=False), # Componente para ler a URL do navegador
    navbar.create_navbar(), # Barra de navegação
    html.Div(id='page-content', children=[]) # Container onde o conteúdo da página será carregado
])

# Callback para atualizar o conteúdo da página com base na URL
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/pagina1':
        return pagina1.layout
    elif pathname == '/pagina2':
        return pagina2.layout
    else:
        # Página inicial ou rota não encontrada, pode redirecionar para pagina1 ou mostrar uma home
        # Aqui, vamos mostrar a página 1 como padrão
        return pagina1.layout

# Bloco para rodar o servidor quando o script é executado diretamente
if __name__ == '__main__':
    # Use 0.0.0.0 para tornar acessível na rede local/externa
    # debug=True ativa o hot-reloading e mensagens de erro detalhadas (desative em produção)
    app.run(host='0.0.0.0', port=8050, debug=True)