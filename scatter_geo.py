import dash
from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

data = {
    "Year": [1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974, 1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018, 2022],
    "Winners": ["Uruguay", "Italy", "Italy", "Uruguay", "Germany", "Brazil", "Brazil", "England", "Brazil", "Germany", "Argentina", "Italy", "Argentina", "Germany", "Brazil", "France", "Brazil", "Italy", "Spain", "Germany", "France", "Argentina"],
    "Runners-up": ["Argentina", "Czechoslovakia", "Hungary", "Brazil", "Hungary", "Sweden", "Czechoslovakia", "Germany", "Italy", "Netherlands", "Netherlands", "Germany", "Germany", "Argentina", "Italy", "Brazil", "Germany", "France", "Netherlands", "Argentina", "Croatia", "France"],
    "Host": ["Uruguay", "Italy", "France", "Brazil", "Switzerland", "Sweden", "Chile", "England", "Mexico", "Germany", "Argentina", "Spain", "Mexico", "Italy", "United States", "France", "Japan", "Germany", "South Africa", "Brazil", "Russia", "Qatar"]
}
df = pd.DataFrame(data)

win_counts = df["Winners"].value_counts().reset_index()
win_counts.columns = ["Country", "Wins"]
win_counts["Wins"] = win_counts["Wins"].astype(str)
win_counts["Country"] = win_counts["Country"].replace("England", "United Kingdom")

color_scale = {
    "1": "blue",
    "2": "green",
    "3": "yellow",
    "4": "orange",
    "5": "red"
}

fig = px.choropleth(
    win_counts,
    locations="Country",
    locationmode="country names",
    color="Wins",
    color_discrete_map=color_scale,
    title="Countries That Have Won the FIFA World Cup"
)

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([
    html.H1("World Cup Winners Dashboard"),

    html.Label("Select a Year:"),
    dcc.Dropdown(
        id="year-dropdown",
        options=[{"label": year, "value": year} for year in df["Year"].unique()],
        value=df["Year"].min(),
        clearable=False
    ),
    
    html.Div(id="winner-runnerup-output", style={"margin-top": "20px", "font-size": "18px"}),
    
    dcc.Graph(figure=fig)
])

@app.callback(
    Output("winner-runnerup-output", "children"),
    Input("year-dropdown", "value")
)
def update_winner_runnersup(year):
    row = df[df["Year"] == year].iloc[0]
    winner = row["Winners"]
    runner_up = row["Runners-up"]
    return html.Span([
        html.B(f"In {year}, "),
        html.Span(f"{winner} ", style={"color": "red", "font-weight": "bold"}),
        "won the World Cup and ",
        html.Span(f"{runner_up} ", style={"color": "blue", "font-weight": "bold"}),
        "was the runner-up."
    ])

if __name__ == "__main__":
    app.run(debug=True)
