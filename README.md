# Movie-Recommendation-System

Following a Data Analyst Training at Wild Code School, this is the second projet that my colleagues and I have built with the aim to improve our Data Manipulation and Algorithm skills. We took 6 weeks to build this recommendation system. 

<b>To put in a nutshell...</b> 

The aim of this project is to create a movie recommendation system to a theater located at Creuse (a department in France). They want to increase their profits and they would like to send notifications to the customers by SMS or e-mails. 

Our team is in a situation of cold start. However, the customer gave us a database of movies based from the IMDb platform. In this way, we had to manipulate those data in order to clean it and after that, we started to develop the algorithm. 

##

<h1> The code of the project below</h1>

<b>Homepage</b> 


~~~~
from dash import Dash, dcc, html, callback, Input, Output
import dash_bootstrap_components as dbc

flexflix='https://cdn.discordapp.com/attachments/960528151765717054/973191422830321705/F_4.png'

sklearn='https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Scikit_learn_logo_small.svg/1280px-Scikit_learn_logo_small.svg.png'
plotly='https://res.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_256,w_256,f_auto,q_auto:eco,dpr_1/wgshctk7kjdxl6omgwra'
trello='https://www.koweb.fr/images/e/4/5/e/8/e45e8c84306c6ffcd92344bb868bdecd327fa62a-trello.png?g-ab66bb8c'
python='https://www.pngmart.com/files/7/Python-PNG-File.png'
jupyter='https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Jupyter_logo.svg/1767px-Jupyter_logo.svg.png'
bootstrap='https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Bootstrap_logo.svg/512px-Bootstrap_logo.svg.png'
logohtml='https://cdn.pixabay.com/photo/2017/08/05/11/16/logo-2582748_1280.png'
css='https://cdn.pixabay.com/photo/2017/08/05/11/16/logo-2582747_1280.png'
imdb='https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/IMDb_Logo_Square.svg/2048px-IMDb_Logo_Square.svg.png'
tmdb='https://www.programmableweb.com/sites/default/files/TMDb.jpg'
scrum='https://onlyweb-formation.com/uploads/mod_logo/methode_agile1.png'
discord='https://upload.wikimedia.org/wikipedia/fr/8/80/Logo_Discord_2015.png'
collab='https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Google_Colaboratory_SVG_Logo.svg/2560px-Google_Colaboratory_SVG_Logo.svg.png'
bruce="https://cdn.discordapp.com/attachments/960528151765717054/972137254434791464/unknown.png"
denzel="https://media.discordapp.net/attachments/960528151765717054/972137855721803827/denzel.jpg"
leo="https://cdn.discordapp.com/attachments/960528151765717054/972139358394122250/Capture_decran_2022-05-06_a_16.14.15.png"
trinity="https://cdn.discordapp.com/attachments/960528151765717054/973265638271377479/Trinity.png"


acc = Dash(__name__, 
            external_stylesheets=[dbc.themes.SOLAR],
            meta_tags=[
                {"name": "viewport", "content": "width=device-width, initial-scale=1"}
            ],
)

acc.layout = html.Div([

    html.Div([ 
        html.A([       
            html.P("Accueil", className='ici'),
        ]),
        html.A([
            html.P("Top film", className='top'),
        ],href="http://127.0.0.1:8002/"),
        html.A([
            html.P("Dashboard", className='focus'),
        ],href="http://127.0.0.1:8003/"),
        html.A([
            html.P("Recommandations", className='algo'),
        ],href="http://127.0.0.1:8007/"),
        html.A([
            html.P("Next step", className='step'),
        ],href="http://127.0.0.1:8008/"),
    ], className='nav'),
    
    html.H1("The FlexFlix Project", className='titre2'),
    html.H3("Bienvenue chez FlexFlix pour trouver votre bonheur cinématographique!", className='section-titre'),
        
    html.Div([
        html.Img(src=flexflix, className='logo-accueil')

    ], className='div-logo-accueil'),
    
    
    html.H3("Notre team", className='sec-titre'),

        html.Div([
        
        html.A([
            dbc.Col([
                html.Img(src=bruce, className='crew'),
                html.H5('Romaric - Bruce'),
                html.H6('SCRUM Master')
                ], lg=3, md=12, sm=12, className='div-crew')
             ], href='https://www.linkedin.com/in/romaric-ledoux-b7625b190/', className='link'),
        
        html.A([
            dbc.Col([        
        html.Img(src=denzel, className='crew'),
                html.H5('Niven - Denzel'),
                html.H6('Co-Product Owner')
                ], lg=3, md=12, sm=12, className='div-crew')
             ], href='https://www.linkedin.com/in/niven-rayapen-058ba649/', className='link'),      

        html.A([
            dbc.Col([
        html.Img(src=leo, className='crew'),
                html.H5('Leonardo - Leo'),
                html.H6('Co-Product Owner')
                ], lg=3, md=12, sm=12, className='div-crew')
             ], href='https://www.linkedin.com/in/leonardossouza/', className='link'),   

        html.A([
            dbc.Col([        
        html.Img(src=trinity, className='crew'),
                html.H5('Marine - Trinity'),
                html.H6('Team Member - Dash Padawan')
                ], lg=3, md=12, sm=12, className='div-crew')
             ], href='https://www.linkedin.com/in/marine-pernici/', className='link'),    
    
    
    ], className='team'),

    html.H3("Nos outils", className='sec-titre'),
    html.Div([
    html.Img(src=imdb, className='logo'),
    html.Img(src=tmdb, className='logo'),

    html.Img(src=python, className='logo'),
    html.Img(src=plotly, className='logo'),
    html.Img(src=sklearn, className='logo'),
    html.Img(src=logohtml, className='logo'),
    html.Img(src=css, className='logo'),
    html.Img(src=bootstrap, className='logo'),
    html.Img(src=jupyter, className='logo'),

    html.Img(src=collab, className='logo'),
    html.Img(src=scrum, className='logo'),
    html.Img(src=discord, className='logo'),
    html.Img(src=trello, className='logo'),


    

    ], className='team')






])

  


if __name__ == '__main__':
    acc.run_server(debug=True, port=8001)
~~~~

<div style="display: inline_block"><br>
	<img align="center" alt="H" src="https://github.com/leonardodasilvasouza/Movie-Recommendation-System/blob/main/homepage.png?raw=true">
</div>

#

<b>Top Films</b> 

~~~~
#import random
import pandas as pd
from dash import Dash, dcc, html, callback, Input, Output
import dash_bootstrap_components as dbc
import numpy as np

df_top60 = pd.read_csv('Datas\df_top60.csv')
df_french = pd.read_csv('Datas\df_french.csv')
df_rent=pd.read_csv('Datas\df_rent.csv')

#df_top100['imdb_link'] = df_top100['tconst'].apply(lambda x : "https://www.imdb.com/title/"+x+"/?ref_=hm_tpks_tt_i_1_pd_tp1_cp")
#df_french['imdb_link'] = df_french['tconst'].apply(lambda x : "https://www.imdb.com/title/"+x+"/?ref_=hm_tpks_tt_i_1_pd_tp1_cp")
#df_rent['imdb_link'] = df_rent['tconst'].apply(lambda x : "https://www.imdb.com/title/"+x+"/?ref_=hm_tpks_tt_i_1_pd_tp1_cp")




multi = Dash(__name__, 
            external_stylesheets=[dbc.themes.SOLAR],
            meta_tags=[
                {"name": "viewport", "content": "width=device-width, initial-scale=1"}
            ],
)

multi.layout = html.Div([
    # represents the browser address bar and doesn't render anything
    dcc.Location(id='url', refresh=False),

        # content will be rendered in this element
    html.Div([ 
        html.A([       
            html.P("Accueil", className='acc'),
        ],href="http://127.0.0.1:8001/"),
        html.A([
            html.P("Top film", className='ici'),
        ]),
        html.A([
            html.P("Dashboard", className='focus'),
        ],href="http://127.0.0.1:8003/"),
        html.A([
            html.P("Recommandations", className='algo'),
        ],href="http://127.0.0.1:8007/"),
        html.A([
            html.P("Next step", className='step'),
        ],href="http://127.0.0.1:8008/"),
    ], className='nav'),
    
    html.H1("The FlexFlix Project", className='titre2'),
    html.H3("Analyse exploratoire : Top film", className='section-titre'),

    html.H5("Les meilleurs films de tous les temps", className = 'sec-titre'), 
    html.Div(id='movies-carousel', className='wrapper'),
    
    html.H5("Les meilleurs films français de tous les temps", className = 'sec-titre'),
    html.Div(id='movies-carousel2', className='wrapper'),
    
    html.H5("Les films les plus rentables (2012-2022)", className = 'sec-titre'),
    html.Div(id='movies-carousel3', className='wrapper')
])

@callback(  Output('movies-carousel', 'children'),
            Output('movies-carousel2', 'children'),
            Output('movies-carousel3', 'children'),
            Input('url', 'pathname') #input pas nécessaire
)
def display_page(pathname):

        output = []
        list_posters = df_top60.poster_path
        list_link=df_top60.imdb_link
        list_title=df_top60.title
        list_year=df_top60.startYear
        sections = [1, 2, 3, 4, 5]
        nb_movies = 12

        for i in range(len(sections)):
            
            href_before = sections[sections.index(i+1)-1]
            href_next = sections[i]+1 if sections[i]+1 <= len(sections) else 1

            images = [html.A([
                        html.Div([
                            html.Img(src=list_posters[n], className='item', title=list_title[n] + ' - ' + str(list_year[n]))
                        ], className='item-container')
                    ],href=list_link[n], className='link') 
                    for n in range(nb_movies*(i+1) - nb_movies, nb_movies*(i+1))]
            
            section = html.Section([
                html.A(href=f'#top_int{href_before}', className="arrow_btn1"),
                *images,
                html.A(href=f'#top_int{href_next}', className="arrow_btn2")
                ], id=f'top_int{i+1}')

            output.append(section)

        output2 = []
        list_posters2 = df_french.poster_path
        list_link2=df_french.imdb_link
        list_title2=df_french.title
        list_year2=df_french.startYear
        for i in range (len(sections)):
            
            href_before = sections[sections.index(i+1)-1]
            href_next = sections[i]+1 if sections[i]+1 <= len(sections) else 1

            images = [html.A([
                        html.Div([
                            html.Img(src=list_posters2[n], className='item', title=list_title2[n] + ' - ' + str(list_year2[n]))
                        ], className='item-container')
                    ],href=list_link2[n], className='link') 
                    for n in range(nb_movies*(i+1) - nb_movies, nb_movies*(i+1))]

            section = html.Section([
                html.A(href=f'#top_fr{href_before}', className="arrow_btn1"),
                *images,
                html.A(href=f'#top_fr{href_next}', className="arrow_btn2")
                ], id=f'top_fr{i+1}')

            output2.append(section)

        output3 = []
        list_posters3 = df_rent.poster_path
        list_link3=df_rent.imdb_link
        list_title3=df_rent.title
        list_year3=df_rent.startYear
        for i in range (len(sections)):
            
            href_before = sections[sections.index(i+1)-1]
            href_next = sections[i]+1 if sections[i]+1 <= len(sections) else 1

            images = [html.A([
                        html.Div([
                            html.Img(src=list_posters3[n], className='item', title=list_title3[n] + ' - ' + str(list_year3[n]))
                        ], className='item-container')
                    ],href=list_link3[n], className='link') 
                    for n in range(nb_movies*(i+1) - nb_movies, nb_movies*(i+1))]

            section = html.Section([
                html.A(href=f'#top_${href_before}', className="arrow_btn1"),
                *images,
                html.A(href=f'#top_${href_next}', className="arrow_btn2")
                ], id=f'top_${i+1}')

            output3.append(section)
        


        return tuple(output), tuple(output2), tuple(output3),  
    
   #else :
       # return

  


if __name__ == '__main__':
    multi.run_server(debug=True, port=8002)
 
~~~~
<div style="display: inline_block"><br>
	<img align="center" alt="H" src="https://github.com/leonardodasilvasouza/Movie-Recommendation-System/blob/main/topfilm.png?raw=true">
</div>

#

<b>Top Films</b> 

~~~~
#import random
import pandas as pd
from dash import Dash, dcc, html, callback, Input, Output
import dash_bootstrap_components as dbc
import numpy as np

df_top60 = pd.read_csv('Datas\df_top60.csv')
df_french = pd.read_csv('Datas\df_french.csv')
df_rent=pd.read_csv('Datas\df_rent.csv')

#df_top100['imdb_link'] = df_top100['tconst'].apply(lambda x : "https://www.imdb.com/title/"+x+"/?ref_=hm_tpks_tt_i_1_pd_tp1_cp")
#df_french['imdb_link'] = df_french['tconst'].apply(lambda x : "https://www.imdb.com/title/"+x+"/?ref_=hm_tpks_tt_i_1_pd_tp1_cp")
#df_rent['imdb_link'] = df_rent['tconst'].apply(lambda x : "https://www.imdb.com/title/"+x+"/?ref_=hm_tpks_tt_i_1_pd_tp1_cp")




multi = Dash(__name__, 
            external_stylesheets=[dbc.themes.SOLAR],
            meta_tags=[
                {"name": "viewport", "content": "width=device-width, initial-scale=1"}
            ],
)

multi.layout = html.Div([
    # represents the browser address bar and doesn't render anything
    dcc.Location(id='url', refresh=False),

        # content will be rendered in this element
    html.Div([ 
        html.A([       
            html.P("Accueil", className='acc'),
        ],href="http://127.0.0.1:8001/"),
        html.A([
            html.P("Top film", className='ici'),
        ]),
        html.A([
            html.P("Dashboard", className='focus'),
        ],href="http://127.0.0.1:8003/"),
        html.A([
            html.P("Recommandations", className='algo'),
        ],href="http://127.0.0.1:8007/"),
        html.A([
            html.P("Next step", className='step'),
        ],href="http://127.0.0.1:8008/"),
    ], className='nav'),
    
    html.H1("The FlexFlix Project", className='titre2'),
    html.H3("Analyse exploratoire : Top film", className='section-titre'),

    html.H5("Les meilleurs films de tous les temps", className = 'sec-titre'), 
    html.Div(id='movies-carousel', className='wrapper'),
    
    html.H5("Les meilleurs films français de tous les temps", className = 'sec-titre'),
    html.Div(id='movies-carousel2', className='wrapper'),
    
    html.H5("Les films les plus rentables (2012-2022)", className = 'sec-titre'),
    html.Div(id='movies-carousel3', className='wrapper')
])

@callback(  Output('movies-carousel', 'children'),
            Output('movies-carousel2', 'children'),
            Output('movies-carousel3', 'children'),
            Input('url', 'pathname') #input pas nécessaire
)
def display_page(pathname):

        output = []
        list_posters = df_top60.poster_path
        list_link=df_top60.imdb_link
        list_title=df_top60.title
        list_year=df_top60.startYear
        sections = [1, 2, 3, 4, 5]
        nb_movies = 12

        for i in range(len(sections)):
            
            href_before = sections[sections.index(i+1)-1]
            href_next = sections[i]+1 if sections[i]+1 <= len(sections) else 1

            images = [html.A([
                        html.Div([
                            html.Img(src=list_posters[n], className='item', title=list_title[n] + ' - ' + str(list_year[n]))
                        ], className='item-container')
                    ],href=list_link[n], className='link') 
                    for n in range(nb_movies*(i+1) - nb_movies, nb_movies*(i+1))]
            
            section = html.Section([
                html.A(href=f'#top_int{href_before}', className="arrow_btn1"),
                *images,
                html.A(href=f'#top_int{href_next}', className="arrow_btn2")
                ], id=f'top_int{i+1}')

            output.append(section)

        output2 = []
        list_posters2 = df_french.poster_path
        list_link2=df_french.imdb_link
        list_title2=df_french.title
        list_year2=df_french.startYear
        for i in range (len(sections)):
            
            href_before = sections[sections.index(i+1)-1]
            href_next = sections[i]+1 if sections[i]+1 <= len(sections) else 1

            images = [html.A([
                        html.Div([
                            html.Img(src=list_posters2[n], className='item', title=list_title2[n] + ' - ' + str(list_year2[n]))
                        ], className='item-container')
                    ],href=list_link2[n], className='link') 
                    for n in range(nb_movies*(i+1) - nb_movies, nb_movies*(i+1))]

            section = html.Section([
                html.A(href=f'#top_fr{href_before}', className="arrow_btn1"),
                *images,
                html.A(href=f'#top_fr{href_next}', className="arrow_btn2")
                ], id=f'top_fr{i+1}')

            output2.append(section)

        output3 = []
        list_posters3 = df_rent.poster_path
        list_link3=df_rent.imdb_link
        list_title3=df_rent.title
        list_year3=df_rent.startYear
        for i in range (len(sections)):
            
            href_before = sections[sections.index(i+1)-1]
            href_next = sections[i]+1 if sections[i]+1 <= len(sections) else 1

            images = [html.A([
                        html.Div([
                            html.Img(src=list_posters3[n], className='item', title=list_title3[n] + ' - ' + str(list_year3[n]))
                        ], className='item-container')
                    ],href=list_link3[n], className='link') 
                    for n in range(nb_movies*(i+1) - nb_movies, nb_movies*(i+1))]

            section = html.Section([
                html.A(href=f'#top_${href_before}', className="arrow_btn1"),
                *images,
                html.A(href=f'#top_${href_next}', className="arrow_btn2")
                ], id=f'top_${i+1}')

            output3.append(section)
        


        return tuple(output), tuple(output2), tuple(output3),  
    
   #else :
       # return

  


if __name__ == '__main__':
    multi.run_server(debug=True, port=8002)
 
~~~~
<div style="display: inline_block"><br>
	<img align="center" alt="H" src="https://github.com/leonardodasilvasouza/Movie-Recommendation-System/blob/main/topfilm.png?raw=true">
</div>

#

<b>Graphiques</b> 

~~~~
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
 
~~~~
<div style="display: inline_block"><br>
	<img align="center" alt="H" src="https://github.com/leonardodasilvasouza/Movie-Recommendation-System/blob/main/graphiques.png?raw=true">
</div>

#

<b>Recommandation</b> 

~~~~
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import pandas as pd
from sklearn.neighbors import NearestNeighbors
import dash_bootstrap_components as dbc
import numpy as np
from google_trans_new import google_translator

#data
df_alg = pd.read_csv('Datas\df_alg.csv')

list_dropdown = df_alg.sort_values('title')

X = df_alg[['averageRating', 'startYear_10', 'runtimeMinutes2', 'region_fac', 
                    'Action', 'Adult', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime',         
                    'Documentary', 'Drama', 'Family', 'Fantasy', 'Film-Noir',
                    'History', 'Horror', 'Music', 'Musical', 'Mystery', 'News',
                    'Romance', 'Sci-Fi', 'Sport', 'Thriller', 'War', 'Western']]

distanceKNN5 = NearestNeighbors(n_neighbors=7).fit(X)
trans = google_translator()


#initialisation de l'app
alg=dash.Dash(__name__,
                external_stylesheets=[dbc.themes.SOLAR],
                meta_tags=[
                    {"name": "viewport", "content": "width=device-width, initial-scale=1"}
                ],
)

#back-end
alg.layout = html.Div([
    
    html.Div([ 
        html.A([       
            html.P("Accueil", className='acc'),
        ],href="http://127.0.0.1:8001/"),
        html.A([
            html.P("Top film", className='top'),
        ],href="http://127.0.0.1:8002/"),
        html.A([
            html.P("Dashboard", className='focus'),
        ],href="http://127.0.0.1:8003/"),
        html.A([
            html.P("Recommandations", className='ici'),
        ]),
        html.A([
            html.P("Next step", className='step'),
        ],href="http://127.0.0.1:8008/"),
    ], className='nav'),

    html.H1("The FlexFlix Project", className='titre2'),
    html.H3("Algorithme de recommandation de films", className='section-titre'),
        
        
        html.Div([
            html.H5("Choisissez un film que vous avez aimé dans la liste suivante pour savoir quels films nous vous recommandons: ", className='sous-titre'),
            dcc.Dropdown(
                options = [{'label' : t, 'value' : t}
                            for t in list(list_dropdown.title)],
                placeholder="Selectionnez un film",
                multi=False,
                clearable=True,
                id="dropdown-component"       
            )
        ], className='menu'),

    dbc.Row([
        dbc.Col([
            html.Div([
                dcc.Loading([
                    html.A([
                        html.Div([
                            html.Img(
                                id=f'poster{i}',
                                className='image',
                            ),
                            html.H4(
                                id=f'titre{i}',
                                className='titre-film',
                            ),
                            html.P(
                                id=f'overview{i}',
                                className='rec-overview',
                            ),
                            html.H5(
                                id=f'year{i}',
                                className='year'
                            ),
                            html.H5(
                                id=f'genre{i}',
                                className='genre',
                            )
                            ],className = 'rec-container'),
                    ], id=f'link{i}', className='link'),
                ], color='aquamarine'),
            ]),
        ], lg=2, md=12, sm=12) for i in range(1,7)], className='row-alg')

], className ='body')

@alg.callback(
    *[(Output(component_id=f'poster{i}', component_property='src'),
    Output(component_id=f'titre{i}', component_property='children'),
    Output(component_id=f'overview{i}', component_property='children'),
    Output(component_id=f'year{i}', component_property='children'),
    Output(component_id=f'genre{i}', component_property='children'),
    Output(component_id=f'link{i}', component_property='href')) for i in range (1,7)],
    
    Input(component_id='dropdown-component', component_property='value'),
    prevent_initial_call=True
)
def recommandation (title_t100):
    neighbors = distanceKNN5.kneighbors(df_alg[['averageRating', 'startYear_10', 'runtimeMinutes2', 'region_fac', 
                    'Action', 'Adult', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime',         
                    'Documentary', 'Drama', 'Family', 'Fantasy', 'Film-Noir',
                    'History', 'Horror', 'Music', 'Musical', 'Mystery', 'News',
                    'Romance', 'Sci-Fi', 'Sport', 'Thriller', 'War', 'Western']][df_alg.title.isin([title_t100])])


    output_tuple=[]

    for i in range (7) :   
        if int(neighbors[1][0][i])  != df_alg.index[df_alg.title == title_t100][0] :  

            image=list(df_alg.poster_path[df_alg.index.isin([neighbors[1][0][i]])])[0]
            titre=str(list(df_alg.title[df_alg.index.isin([neighbors[1][0][i]])])[0])
            year=str(list(df_alg.startYear[df_alg.index.isin([neighbors[1][0][i]])])[0])
            overview = list(df_alg.overview[df_alg.index.isin([neighbors[1][0][i]])])[0] [0:101] + '...'
            genre=list(df_alg.genres[df_alg.index.isin([neighbors[1][0][i]])])
            link="https://www.imdb.com/title/"+str(list(df_alg.tconst[df_alg.index.isin([neighbors[1][0][i]])])[0])+"/?ref_=hm_tpks_tt_i_1_pd_tp1_cp"

            output_tuple.append(image)
            output_tuple.append(titre)            
            output_tuple.append(trans.translate(overview, lang_src = 'en', lang_tgt = 'fr'))
            output_tuple.append(year)
            output_tuple.append(genre)
            output_tuple.append(link)

    return  output_tuple[:36]

if __name__ == '__main__':
    alg.run_server(debug=True, port=8007)
 
~~~~

#

<b>Next Step</b> 

~~~~
from dash import Dash, dcc, html, callback, Input, Output
import dash_bootstrap_components as dbc

ml='https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Scikit_learn_logo_small.svg/1280px-Scikit_learn_logo_small.svg.png'
plotly='https://res.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_256,w_256,f_auto,q_auto:eco,dpr_1/wgshctk7kjdxl6omgwra'
trello='https://www.koweb.fr/images/e/4/5/e/8/e45e8c84306c6ffcd92344bb868bdecd327fa62a-trello.png?g-ab66bb8c'
python='https://www.pngmart.com/files/7/Python-PNG-File.png'
jupyter='https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Jupyter_logo.svg/1767px-Jupyter_logo.svg.png'
bootstrap='https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Bootstrap_logo.svg/512px-Bootstrap_logo.svg.png'
logohtml='https://cdn.pixabay.com/photo/2017/08/05/11/16/logo-2582748_1280.png'
css='https://cdn.pixabay.com/photo/2017/08/05/11/16/logo-2582747_1280.png'
imdb='https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/IMDb_Logo_Square.svg/2048px-IMDb_Logo_Square.svg.png'
tmdb='https://www.programmableweb.com/sites/default/files/TMDb.jpg'
flexflix='https://cdn.discordapp.com/attachments/960528151765717054/973191422830321705/F_4.png'
scrum='https://onlyweb-formation.com/uploads/mod_logo/methode_agile1.png'
discord='https://upload.wikimedia.org/wikipedia/fr/8/80/Logo_Discord_2015.png'
collab='https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Google_Colaboratory_SVG_Logo.svg/2560px-Google_Colaboratory_SVG_Logo.svg.png'



next = Dash(__name__, 
            external_stylesheets=[dbc.themes.SOLAR],
            meta_tags=[
                {"name": "viewport", "content": "width=device-width, initial-scale=1"}
            ],
)

next.layout = html.Div([

    html.Div([ 
        html.A([       
            html.P("Accueil", className='acc'),
        ],href="http://127.0.0.1:8001/"),
        html.A([
            html.P("Top film", className='top'),
        ],href="http://127.0.0.1:8002/"),
        html.A([
            html.P("Dashboard", className='focus'),
        ],href="http://127.0.0.1:8003/"),
        html.A([
            html.P("Recommandations", className='algo'),
        ],href="http://127.0.0.1:8007/"),
        html.A([
            html.P("Next step", className='ici'),
        ]),
    ], className='nav'),
    
    html.H1("The FlexFlix Project", className='titre2'),
    html.H3("Pour aller plus loin ...", className='section-titre'),
        
        html.Div([
        
        html.A([
            dbc.Col([
                html.H3("Analyse de la base de données", className='next-titre'),
                html.Img(src="https://blog.businessdecision.com/wp-content/uploads/2020/09/experience-client-performance-835x400-1.jpg", className='next'),
                html.H5('↬ Prendre en compte des films plus confidentiels, peu connus du grand public mais de grande qualité et qui gagneraient à être découvert.', className='next-container'),
                html.H5('↬ Analyse exploratoire plus approfondie du cinéma français.', className='next-container'),
                ], lg=4, md=12, sm=12, className='div-next')
             ], className='link'),
        
        html.A([
            dbc.Col([        
                html.H3("Algorithme de recommandation", className='next-titre'),
                html.Img(src="https://www.ionos.fr/digitalguide/fileadmin/DigitalGuide/Teaser/deep-learning-vs-machine-learning-t.jpg", className='next'),
                html.H5('↬ Agréger plusieurs modèles complémentaires prenant aussi en compte les acteurs et actrices, les réalisateurs ...', className='next-container'),
                html.H5('↬ Utilisation du NLP pour ajouter les synopsis dans les critères utilisés pour la recommandation.', className='next-container'),
                ], lg=4, md=12, sm=12, className='div-next')
             ], className='link'),      

        html.A([
            dbc.Col([
                html.H3("Expérience utilisateur", className='next-titre'),
                html.Img(src="https://my.kapook.com/imagescontent/fb_img/3/s_109673_8040.jpg", className='next'),
                html.H5('↬ Interface entièrement en français (posters, résumés, genres).', className='next-container'),
                html.H5('↬ Suivi des comportements utilisateurs.', className='next-container'),
                html.H5('↬ Envoi de notifications personnalisées aux clients.', className='next-container'),
                ], lg=4, md=12, sm=12, className='div-next')
             ], className='link'),     
    
    
    ], className='team2'),

    html.H3("Nos outils", className='sec-titre'),
    html.Div([
    html.Img(src=imdb, className='logo'),
    html.Img(src=tmdb, className='logo'),

    html.Img(src=python, className='logo'),
    html.Img(src=plotly, className='logo'),
    html.Img(src=ml, className='logo'),
    html.Img(src=logohtml, className='logo'),
    html.Img(src=css, className='logo'),
    html.Img(src=bootstrap, className='logo'),
    html.Img(src=jupyter, className='logo'),

    html.Img(src=collab, className='logo'),
    html.Img(src=scrum, className='logo'),
    html.Img(src=discord, className='logo'),
    html.Img(src=trello, className='logo'),


    

    ], className='team')






])

  


if __name__ == '__main__':
    next.run_server(debug=True, port=8008)
 
~~~~
<div style="display: inline_block"><br>
	<img align="center" alt="H" src="https://github.com/leonardodasilvasouza/Movie-Recommendation-System/blob/main/next.png?raw=true">
</div>
