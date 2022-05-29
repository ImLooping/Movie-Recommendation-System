#import random
from tkinter import Y, font
from turtle import color
import pandas as pd
from dash import Dash, dcc, html, callback, Input, Output
import dash_bootstrap_components as dbc
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

df_graph_actors = pd.read_csv("Datas\df_graph_actors.csv")
df_graph_actress = pd.read_csv("Datas\df_graph_actress.csv")
df_genre = pd.read_csv("Datas\df_genre.csv")
df_graph_directors = pd.read_csv("Datas\df_graph_directors.csv")
df_graph_rent = pd.read_csv("Datas\df_graph_rent.csv")


'''df_d8_popmed = pd.read_csv('Datas\df_d8_popmed.csv')
mask = df_d8_popmed.index[df_d8_popmed.revenue <= 0]
df_d8_popmed.drop(index=mask, inplace=True)
df_d8_popmed = df_d8_popmed[df_d8_popmed.startYear >= 2012]
df_d8_popmed['popularity'] = df_d8_popmed['popularity'].apply(lambda x : 9 if x> df_d8_popmed['popularity'].quantile(0.9)
                                                              else 8 if x> df_d8_popmed['popularity'].quantile(0.8)
                                                              else 7 if x> df_d8_popmed['popularity'].quantile(0.7)
                                                              else 6 if x> df_d8_popmed['popularity'].quantile(0.6)
                                                              else 5 if x> df_d8_popmed['popularity'].quantile(0.5)
                                                              else 4 if x> df_d8_popmed['popularity'].quantile(0.4)
                                                              else 3 if x> df_d8_popmed['popularity'].quantile(0.3)
                                                              else 2 if x> df_d8_popmed['popularity'].quantile(0.2)
                                                              else 1 if x> df_d8_popmed['popularity'].quantile(0.1)
                                                              else 0)'''



fig = make_subplots(rows=1, cols=2,
                    #subplot_titles=("Acteurs", "Actrices"),
                    horizontal_spacing=0.01)

fig.add_trace(go.Bar(
    y=df_graph_actors.primaryName,
    x=df_graph_actors.apparition,
    orientation='h',
    hovertemplate = '<b>%{y}</b><br>%{x} films<br><extra></extra>',
    marker=dict(
        color=px.colors.sequential.Viridis),
    ),
    row=1, col=1)

fig.update_xaxes(range=[9,2],
                row=1, col=1,
                showgrid=False,
                color= 'cadetblue',
                tickfont=dict(family='sans-serif', size=18))

fig.update_yaxes(
                row=1, col=1,
                showgrid=False,
                color= 'cadetblue',
                tickfont=dict(family='sans-serif', size=18))

fig.add_trace(go.Bar(
    y=df_graph_actress.primaryName,
    x=df_graph_actress.apparition,
    orientation='h',
    #text=" " + df_graph_actress.primaryName,
    #textposition='outside',
    #textfont=dict(size=22, 
            #color="cadetblue",
            #family= "sans-serif"),
    hovertemplate = '<b>%{y}</b><br>%{x} films<br><extra></extra>',
    marker=dict(
        color=px.colors.sequential.Viridis),
    ),
    row=1, col=2)
          
fig.update_yaxes(side='right',
                row=1, col=2,
                #showticklabels=False,
                #ticklabelposition='inside',
                showgrid=False,
                color= 'cadetblue',
                tickfont=dict(family='sans-serif', size=18))

fig.update_xaxes(range=[2,7],
                row=1, col=2,
                showgrid=False,
                color= 'cadetblue',
                tickfont=dict(family='sans-serif', size=18))

fig.update_layout(
        height=250,
        #width = 1200,
        showlegend=False,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(t=0, b=0, l=0, r=0))

fig2 = go.Figure()

fig2.add_trace(go.Treemap(
    labels = df_genre['genre'],
    parents = ['2012-2022' for i in df_genre.genre],
    values = df_genre['count'],
        textinfo = "label+value+percent root",
        textposition='middle center',
        hoverinfo = 'skip',
        texttemplate='<b>%{label}</b><br>%{value} films<br>Ratio : %{percentRoot}',
        insidetextfont=dict(size=16),           
        marker=dict(
            colorscale='Viridis'),
))
fig2.update_layout(margin = dict(t=0, l=0, r=0, b=0),                 
    height=830,
    )


fig3=go.Figure()
fig3.add_trace(go.Scatter(    
    x=df_graph_rent['revenue'],
    y=df_graph_rent['averageRating'],
    text=df_graph_rent["title"],
    customdata=df_graph_rent["popularity"],
    hovertemplate = '<b>%{text}</b><br>' +
                    'Recette=%{x:$.2s}<br>'+
                    'Note=%{y}<br>'+
                    'Popularité=%{customdata}<br>' + 
                    '<extra></extra>',    
    mode='markers',
    marker_color=df_graph_rent['popularity'],
    marker=dict(
        colorscale='Viridis',
        showscale=True,
        line=dict(
                color='#bddf26',
                width=0.5),
        colorbar=dict(
                  x=-0.13,
                  title_font_color='cadetblue',
                  title_font_size=20,
                  tickfont_color='cadetblue',
                  tickfont_size=16,
                  title="Popularité",
                  titleside="top",
                  tickmode="array",
                  tickvals=[i for i in range(10)],
                  ticklabelposition='outside bottom'
                  ))))

fig3.update_layout(
        height=450,
        #width=1000, 
        plot_bgcolor= '#073642',
        paper_bgcolor='rgba(0,0,0,0)' ,
        margin=dict(t=0, b=0, l=0, r=0),
        )

fig3.update_xaxes(
    range=[3,10],
    title_font_size=20,
    title_text='Rentabilité (en $)',
    type="log",
    #showgrid=False,
    gridcolor='#002b36',
    color= 'cadetblue',
    tickfont=dict(family='sans-serif', size=16))

fig3.update_yaxes(
    title_font_size=20,
    title_text = 'Notes',
    #showgrid=False,
    gridcolor='#002b36',
    color= 'cadetblue',
    tickfont=dict(family='sans-serif', size=16))
        



fig4=go.Figure()

fig4.add_trace(go.Bar(
    x=df_graph_directors.primaryName,
    y=df_graph_directors.apparition,
    
    hovertemplate = '<b>%{x}</b><br>%{y} films<br><extra></extra>',
    marker=dict(
        color=px.colors.sequential.Viridis),
    ))
          
fig4.update_yaxes(
    title_font_size=20,
    title_text='Nombre de films',
                showgrid=False,
                color= 'cadetblue',
                tickfont=dict(family='sans-serif', size=18),
                ),

fig4.update_xaxes(
                showgrid=False,
                autorange='reversed',
                color= 'cadetblue',
                tickfont=dict(family='sans-serif', size=18),
                tickangle=-40)

fig4.update_layout(
        height=450,
        #width = 1200,
        showlegend=False,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(t=0, b=0, l=0, r=0))


graph = Dash(__name__, 
    external_stylesheets=[dbc.themes.SOLAR],
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}])

graph.layout = html.Div([


    html.Div([ 
        html.A([       
            html.P("Accueil", className='acc'),
        ],href="http://127.0.0.1:8001/"),
        html.A([
            html.P("Top film", className='top'),
        ],href="http://127.0.0.1:8002/"),
        html.A([
            html.P("Dashboard", className='ici'),
        ]),
        html.A([
            html.P("Recommandations", className='algo'),
        ],href="http://127.0.0.1:8007/"),
        html.A([
            html.P("Next step", className='step'),
        ],href="http://127.0.0.1:8008/"),
    ], className='nav'),

    html.H1("The FlexFlix Project", className='titre2'),
    html.H3("Analyse exploratoire : focus 2012-2022", className='section-titre'),



    dbc.Row([

        dbc.Col([

            html.Div([
                html.Div([
                    html.H5('Rentabilité selon la note et la popularité', className='graph-titre'),
                    dcc.Graph(figure=fig3, 
                        config={'displayModeBar': False})
                ], className='graph-actors2'),
    

                html.Div([
                    html.H5('Top 10 réalisateurs', className='graph-titre'),
                    dcc.Graph(figure=fig4, 
                        config={'displayModeBar': False})
                ], className='graph-actors3'),
            ], className='two-graph'),

            html.Div([
            html.H5('Top 10 acteurs et actrices', className='graph-titre'),
            html.Div([
                html.P('Acteurs', className='graph-sous-titre'),
                html.P('Actrices', className='graph-sous-titre'),
            ], className='multiplot'),
            
                dcc.Graph(figure=fig, 
                    config={'displayModeBar': False}),
                html.H6('Nombre de films', className='titre-x'),
            ], className='graph-actors'),



        ], lg=10, md=12, sm=12, className='col1'),

        dbc.Col([
            

            html.Div([
                html.H5('Top 10 genres', className='graph-titre'),
                dcc.Graph(figure=fig2, 
                    config={'displayModeBar': False})
            ], className='graph-actors'),
        ], lg=2, md=12, sm=12, className='col-genre'),

    ], className='row-stat')


])



  


if __name__ == '__main__':
    graph.run_server(debug=True, port=8003)

    