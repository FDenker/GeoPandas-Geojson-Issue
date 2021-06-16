import geopandas as gpd

import json
json.__version__

## This will be empty
gpd.read_file("geopandas_not_found.geojson")


with open("geopandas_not_found.geojson", encoding = 'utf8') as f:
        loaded_json = json.load(f)

## This returns a GeoDataFrame with the right information
correct_gdf=gpd.GeoDataFrame.from_features(loaded_json['features'])

correct_gdf.head(2)
