import dash

# Inicializa a aplicação Dash
# suppress_callback_exceptions=True é necessário para aplicações multi-páginas
# onde os callbacks são definidos em arquivos separados.
app = dash.Dash(__name__, suppress_callback_exceptions=True)

# Para compatibilidade com algumas plataformas de deploy
server = app.server

