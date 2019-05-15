import wunderpy2
import datetime
import pandas as pd

access_token = 'insert access token'
client_id = 'insert cliend id'

api = wunderpy2.WunderApi()
client = api.get_client(access_token, client_id)
completed_tasks_data = client.get_tasks(insert task no., completed=True)

list_completed_at = []

for completed_tasks in completed_tasks_data:
    completed_at = (completed_tasks["completed_at"])
    completed_at = datetime.datetime.strptime(completed_at, '%Y-%m-%dT%H:%M:%S.%fZ')
    completed_at = datetime.datetime.strftime(completed_at, '%Y-%m-%d')
    list_completed_at.append(completed_at)

df = pd.DataFrame(data={'completed_at':list_completed_at})
df = df.groupby(['completed_at']).size().reset_index()

import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[

    dcc.Graph(
        id='Wunderlist_tasks',
        figure={
            'data': [
                {'x': (df["completed_at"]).tolist(), 'y': (df[0]).tolist(), 'type': 'bar', 'name': 'SF'},
            ],
            'layout': {
                'title': 'Wunderlist tasks completed'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)