import folium
import os
import pandas

def elev_color(elev):
    if elev < 1000:
        return 'green'
    elif 1000<= elev < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[38.58,-90.09], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")


data = pandas.read_csv("Volcanoes.txt")
vol_name = list(data["NAME"])
vol_status = list(data["STATUS"])
vol_elev = list(data["ELEV"])
vol_type = list(data["TYPE"])
lon = list(data["LON"])
lat = list(data["LAT"])



for lt,ln,vn,vs,ve,vt in zip(lat,lon,vol_name,vol_status,vol_elev,vol_type):
    
    fg.add_child(folium.CircleMarker(location=[lt,ln], radius=6, popup= "Name: {}\nStatus: {}\nElevation: {}m \nType: {}".format(vn,vs,ve,vt), fill_color=elev_color(ve), color="gray", fill_opacity=0.7))
map.add_child(fg)

map.save("Map1.html")

