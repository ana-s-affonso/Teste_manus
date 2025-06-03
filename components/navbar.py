import dash_bootstrap_components as dbc
from dash import html

def create_navbar():
    """Cria a barra de navegação superior."""
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Página 1", href="/pagina1")),
            dbc.NavItem(dbc.NavLink("Página 2", href="/pagina2")),
        ],
        brand="Meu Dashboard",
        brand_href="/",
        color="primary",
        dark=True,
        className="mb-4", # Adiciona margem inferior
    )
    return navbar

