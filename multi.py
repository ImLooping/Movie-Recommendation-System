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

    