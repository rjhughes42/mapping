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

fgv = folium.FeatureGroup(name="Volcanoes")
fgp = folium.FeatureGroup(name="Population")


data = pandas.read_csv("Volcanoes.txt")
vol_name = list(data["NAME"])
vol_status = list(data["STATUS"])
vol_elev = list(data["ELEV"])
vol_type = list(data["TYPE"])
lon = list(data["LON"])
lat = list(data["LAT"])



for lt,ln,vn,vs,ve,vt in zip(lat,lon,vol_name,vol_status,vol_elev,vol_type):
    
    fgv.add_child(folium.CircleMarker(location=[lt,ln], radius=6, popup= "Name: {}\nStatus: {}\nElevation: {}m \nType: {}".format(vn,vs,ve,vt), fill_color=elev_color(ve), color="gray", fill_opacity=0.7))

fgp.add_child(folium.GeoJson(data=open('world.json','r', encoding='utf-8-sig').read(),
style_function= lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005']< 20000000 else 'red'}))    



map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())

map.save("Map1.html")

