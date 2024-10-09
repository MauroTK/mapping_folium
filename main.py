import folium
import pandas

data = pandas.read_csv("stadiums.txt")
lat = data["LAT"]
lon = data["LON"]
stadium_names = data["NAME"]
capacity = data["CAPACITY"]
region = data["REGION"]


def getMarkerColor(capacity: str):
    if capacity < 70000:
        return "red"
    elif capacity < 80000:
        return "beige"
    else:
        return "darkred"


map = folium.Map(location=(21.815394089921178, -25.460967627613343),
                 zoom_start=4)

fg_NA = folium.FeatureGroup(name="North America")
fg_EU = folium.FeatureGroup(name="Europe")
fg_asia = folium.FeatureGroup(name="Asia")
fg_africa = folium.FeatureGroup(name="Africa")
fg_ocenia = folium.FeatureGroup(name="Oceania")
fg_south_america = folium.FeatureGroup(name="South America")

for lt, ln, name, cap, reg in zip(lat, lon, stadium_names, capacity, region):
    marker = folium.CircleMarker(location=[lt, ln],
                                 color="black",
                                 weight=1,
                                 fill=True,
                                 fill_opacity=0.6,
                                 opacity=1,
                                 popup=f"{name} - {cap}", fill_color=getMarkerColor(cap))
    if reg == "Asia":
        fg_asia.add_child(marker)
    elif reg == "Africa":
        fg_africa.add_child(marker)
    elif reg == "Oceania":
        fg_ocenia.add_child(marker)
    elif reg == "North America":
        fg_NA.add_child(marker)
    elif reg == "Europe":
        fg_EU.add_child(marker)
    elif reg == "South America":
        fg_south_america.add_child(marker)

map.add_child(fg_NA)
map.add_child(fg_EU)
map.add_child(fg_asia)
map.add_child(fg_africa)
map.add_child(fg_ocenia)
map.add_child(fg_south_america)
map.add_child(folium.LayerControl())
map.save("index.html")
