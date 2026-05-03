from pathlib import Path
import json
import plotly.express as px

# Get the directory where this Python script is saved
current_dir = Path(__file__).parent

# Look for the file directly in that same folder (can update with new .geojson 
# files from https://www.usgs.gov/programs/earthquake-hazards)
# The closest earthquake to us in 30 days was in Pigeon Forge at 2.31 magnitude!
path = current_dir / 'earthquake_data_30_April_2026.geojson' 

# Read data as a string and convert to a Python object.
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data['features']

mags, lons, lats, eq_titles = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    
    # Only process the earthquake if it has a valid, positive magnitude
    if mag is not None and mag > 0:
        lon = eq_dict['geometry']['coordinates'][0]
        lat = eq_dict['geometry']['coordinates'][1]
        eq_title = eq_dict['properties']['title']
        
        mags.append(mag)
        lons.append(lon)
        lats.append(lat)
        eq_titles.append(eq_title)

# uses magma coloring, inversed so black is larger, light yellow is smaller
# orthographic projection makes it an interactive globe you can pan around in
title = 'Global Earthquakes, Last 30 Days April 2026'
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title,
        color=mags,
        color_continuous_scale='Magma_r',
        opacity=0.4,
        labels={'color':'Magnitude'},
        projection='orthographic',
        hover_name=eq_titles,
    )
#Coloring of basemap for readability
fig.update_geos(
    showocean=True, oceancolor="MidnightBlue",
    showland=True, landcolor="DarkOliveGreen",
    showlakes=True, lakecolor="MidnightBlue",
    showcountries=True, countrycolor="black"
)
# final layout, dark mode
fig.update_layout(
    title_font_size=28, 
    template='plotly_dark' 
)

# Opens in your default browser
fig.show()