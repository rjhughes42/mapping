import folium
import os

map = folium.Map(location=[38.58,-90.09], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

coord_list = []
vol_name = []

with open ("Volcanoes.txt","r") as file:
    for line in file:
        new_vols = line.strip().split(',')
        coord_list.append(new_vols[8:10])
        vol_name.append(new_vols[2])

coord_list.pop(0)
vol_name.pop(0)




    

for coord,vol in zip(coord_list,vol_name):
        fg.add_child(folium.Marker(location=coord, popup=vol, icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Map1.html")

