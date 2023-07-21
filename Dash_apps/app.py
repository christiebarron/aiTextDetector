#pip install dash plotly

from dash import Dash, html,dash, dash_table, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
import plotly.graph_objs as go


df = pd.read_excel('mydata.xlsx')

app = Dash(__name__)
                
app.layout = html.Div([
    #html.H1(style={'background-image': 'url(https://itchronicles.com/wp-content/uploads/2020/11/where-is-ai-used.jpg)'}),
    html.Div(className='row', children='Visualization of Data According to Teachers',
             style={'background-image': 'url(https://itchronicles.com/wp-content/uploads/2020/11/where-is-ai-used.jpg)','background-size': '100%',
                     'position': 'fixed',
                     'width': '100%',
                     'height': '100%','textAlign': 'center', 'color': 'white', 'fontSize': 30}),

    html.H1(children='Text Analyser with Histogram', style={'textAlign':'center', 'color': 'white', 'fontSize': 30}),
    dcc.Dropdown(df.teacher_name.unique(), id='dropdown-selection',style={"width": "50%"},placeholder="Select a teacher",),
    html.Div(children=[
      dcc.Graph(id="graph1", style={'display': 'inline-block','padding-left':'25%'}),
      dcc.Graph(id="graph2", style={'display': 'inline-block'}),
      dcc.Graph(id="graph3", style={'display': 'inline-block','padding-left':'25%' }),
      dcc.Graph(id="graph4", style={'display': 'inline-block'})
    ]),

    dash_table.DataTable(data=df.to_dict('records'),
                         style_data={ 'border': '1px solid blue' },
                         style_cell={'text-align': 'center', 'margin-bottom':'0'},
                         style_table = {'textAlign': 'center',"margin-left":"25px","margin-right":"25px"},
                        page_size=6),
                         
        
    
    html.H1(children='Cookie policy | Privacy policy | Terms of use |', style={'font-color':'red'})
   
])


@callback(
    Output('graph1', 'figure'),
    Input('dropdown-selection', 'value')
)

def update_graph1(value):
    dff = df[df.teacher_name==value]
    return px.histogram(dff, x='essay_id', y='stop_word_count',title="Stop word count Vs Id")


@app.callback(
    Output('graph2', 'figure'),
    [Input('dropdown-selection', 'value')])
def update_graph2(value):
    dff = df[df.teacher_name==value]
    return px.histogram(dff, x='essay_id', y='total_word_count',title="Total word count Vs Id")


@app.callback(
    Output('graph3', 'figure'),
    [Input('dropdown-selection', 'value')])
def update_graph3(value):
    dff = df[df.teacher_name==value]
    return px.histogram(dff, x='essay_id', y='rare_word_count',title="Rare word count Vs Id")

@app.callback(
    Output('graph4', 'figure'),
    [Input('dropdown-selection', 'value')])
def update_graph4(value): 
    dff = df[df.teacher_name==value]
    return px.histogram(dff, x='essay_id', y='avg_sentence_length',title="Avg sentence length Vs Id")
                        
                        
if __name__ == '__main__':
        app.run_server(debug=True)