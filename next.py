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