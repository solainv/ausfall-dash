import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Daten laden und aufbereiten
df = pd.read_csv('predictive_maintenance.csv')
df.rename(columns={'Type':'type',
 'Air temperature [K]':'air_temp_kelv',
 'Process temperature [K]':'process_temp_kelv',
 'Rotational speed [rpm]':'rotat_speed_rpm',
 'Torque [Nm]':'torque_nm',
 'Tool wear [min]':'tool_wear_min',
 'Target':'target',
 'Failure Type':'failure_type'}, inplace=True)

df['Ausfallzustand'] = df['target'].map({0: 'Kein Ausfall', 1: 'Ausfall'})

# Dash-App erstellen
app = dash.Dash(__name__)
server = app.server
app.title = 'predictive maintenace analysis'

# Layout der App definieren
app.layout = html.Div(
    children=[
        html.Div(
            children=[
                dcc.Graph(
                    id='histogram-1',
                    figure=px.histogram(df, x='rotat_speed_rpm', nbins=30, color='Ausfallzustand').update_layout(
                        xaxis_title='Rotationsgeschwindigkeit',
                        yaxis_title='Häufigkeit',
                        title='Die Rotationsgeschwindigkeit der Maschine in Umdrehungen <br> pro Minute',
                        bargap=0.1,
                        width=600,
                        height=350
                    )
                ),
                dcc.Graph(
                    id='histogram-2',
                    figure=px.histogram(df, x='torque_nm', nbins=30, color='Ausfallzustand').update_layout(
                        xaxis_title='Drehmoment',
                        yaxis_title='Häufigkeit',
                        title='Das Drehmoment der Maschine in Newtonmeter (Nm)',
                        bargap=0.1,
                        width=600,
                        height=350
                    )
                )
            ],
            style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'center', 'justify-content': 'center'}  # Flexbox-Stile für vertikale Anordnung und Zentrierung
        )
    ],
    style={'height': '100vh', 'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}  # Flexbox-Stile für Zentrierung
)

# App starten
if __name__ == '__main__':
    app.run_server(debug=True)
