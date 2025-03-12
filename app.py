import dash
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div("¡Hola desde Dash!", style={"textAlign": "center", "marginTop": "50px"})

if __name__ == "__main__":
    app.run_server(debug=True)
