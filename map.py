import folium
map = folium.Map(location=[38.58,-90.09], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

coord_list = [[45,-88],[25,-69],[47,-119],[26,-97]]

for coord in coord_list:
    fg.add_child(folium.Marker(location=coord, icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Map1.html")

