from dash import Dash, html,dash, dash_table, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
import dash_mantine_components as dmc

df = pd.read_excel('mydata.xlsx')
                   
external_stylesheets = [dmc.theme.DEFAULT_COLORS]
app = Dash(__name__, external_stylesheets=external_stylesheets)



app.layout = html.Div([
    #html.H1(style={'background-image': 'url(https://itchronicles.com/wp-content/uploads/2020/11/where-is-ai-used.jpg)'}),
    html.Div(className='row', children='Visualization of Data According to Teacher',
             style={'textAlign': 'center', 'color': 'blue', 'fontSize': 30}),

   
    html.H1(children='Text Analyser', style={'textAlign':'center', 'color': 'blue', 'fontSize': 30}),
    dcc.Dropdown(df.teacher_name.unique(), 'Celie Stevani', id='dropdown-selection'),
    dcc.Graph(id='graph-content'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=6),
    #dcc.Graph(id=“graph2", style={‘display’: ‘inline-block’}),
    html.H1(children='Cookie policy | Privacy policy | Terms of use |', style={'font-color':'red'})
   
     

])


@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)

def update_graph(value):
    dff = df[df.teacher_name==value]
    return px.histogram(dff, x='essay_id', y='stop_word_count')
                        
                        
if __name__ == '__main__':
    app.run_server(debug=True)