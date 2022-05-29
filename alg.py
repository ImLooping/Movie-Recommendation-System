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