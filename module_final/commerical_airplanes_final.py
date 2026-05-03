# copy and run these next two lines in the terminal to download opensky api
# git clone https://github.com/openskynetwork/opensky-api.git
# pip install -e opensky-api/python
from opensky_api import OpenSkyApi
import plotly.express as px

# create API variable
api = OpenSkyApi()

# create states variable
# https://openskynetwork.github.io/opensky-api/python.html#examples
states = api.get_states()

# build open lists for flight variables per flight (appended from the for loop)
lats, lons, hover_texts, speeds = [], [], [], []

if states:
    # retrieve flight properties/variables through .states function 
    for flight in states.states:
        
        speed_ms = flight.velocity # in meters per second
        
        # append data to lists
        lons.append(flight.longitude)
        lats.append(flight.latitude)
        speeds.append(speed_ms)

        callsign = flight.callsign 
        origin = flight.origin_country 
                
        # determine if climbing, descending, or cruising
        # the "or 0" prevents a "None" return, which isn't a float
        v_rate = flight.vertical_rate or 0
        
        if v_rate == 0:
            flight_status = "Cruising"
        elif v_rate > 0:
            flight_status = "Climbing"
        else:
            flight_status = "Descending"
            
        # build the hover text
        hover_text = f"<b>Callsign:</b> {callsign}<br />"
        hover_text += f"<b>Origin Country:</b> {origin}<br />"
        hover_text += f"<b>Altitude:</b> {flight.baro_altitude} meters<br />"
        hover_text += f"<b>Speed:</b> {speed_ms} m/s<br />"
        hover_text += f"<b>Status:</b> {flight_status}"
            
        hover_texts.append(hover_text)
else:
    exit()

# create data visualization
title = "Live Global Commercial Flights (OpenSky-Network.org Python API)"

fig = px.scatter_geo(lat=lats, 
                     lon=lons, 
                     title=title,
                     hover_name=hover_texts,
                     color=speeds, #velocity mapped to color
                     color_continuous_scale='Bluered', 
                     labels={'color': 'Speed (m/s)'}, 
                     projection='orthographic') #creates globe, pan and zoomable

# trace size and outline 
fig.update_traces(marker=dict(size=4,
                              opacity=0.75,
                              line=dict(width=.3,
                                        color='white')))

# coloring of basemap 
fig.update_geos(showocean=True, oceancolor="MidnightBlue",
                showland=True, landcolor="DarkOliveGreen",
                showlakes=True, lakecolor="MidnightBlue",
                showcountries=True, countrycolor="black")

# final layout, dark mode
fig.update_layout(title_font_size=24,
                  template='plotly_dark',) 

# opens in your default browser
fig.show()