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

    