from dash import Dash, dash_table
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')

app = Dash(__name__)

print(dash_table.__file__)

app.layout = dash_table.DataTable(
    df.to_dict('records'), 
    [{"name": i, "id": i} for i in df.columns],
    id={
        "component": "tralala",
        "aio_id": "trulala"
    }
)

if __name__ == '__main__':
    app.run(debug=True)