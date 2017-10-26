# https://stackoverflow.com/questions/12229580/python-importing-a-sub-package-or-sub-module
# See this post for a discussion of how to import these

import requests
import pandas as pd
from copy import deepcopy

class rw_api_tools:
    def __init__(self):
        """constructor for this class"""
        self.point_template = {
              "type": "Feature",
              "properties": {},
              "geometry": {
                "type": "Point",
                "coordinates": []
              }
            }

        self.date = None

    def get_rw_datasets(self, provider=None):
        url = "https://api.resourcewatch.org/v1/dataset?sort=slug,-provider,userId&status=saved&includes=metadata,vocabulary,widget,layer"
        payload = { "application":"rw", "page[size]": 100000000000}
        res = requests.request("GET", url, params=payload)
        data = res.json()["data"]

        datasets_on_api = {}
        for ix, dset in enumerate(data):
            atts = dset["attributes"]
            metadata = atts["metadata"]
            layers = atts["layer"]
            widgets = atts["widget"]
            tags = atts["vocabulary"]
            datasets_on_api[atts["name"]] = {
                "rw_id":dset["id"],
                "table_name":atts["tableName"],
                "provider":atts["provider"],
                "date_updated":atts["updatedAt"],
                "num_metadata":len(metadata),
                "metadata": metadata,
                "num_layers":len(layers),
                "layers": layers,
                "num_widgets":len(widgets),
                "widgets": widgets,
                "num_tags":len(tags),
                "tags":tags
            ### TO DO: Add in a category for the table columns & aliases
            }

        current_datasets_on_api = pd.DataFrame.from_dict(datasets_on_api, orient='index')
        current_datasets_on_api.index.rename("Dataset", inplace=True)
        current_datasets_on_api.sort_values(by=["date_updated"], inplace=True, ascending = False)

        if provider == None:

            matches = current_datasets_on_api
            print("Total datasets on RW API: ", matches.shape[0])
            return(matches)

        elif (provider in current_datasets_on_api["provider"].unique()):

            match_ix = current_datasets_on_api["provider"]==provider
            matches = current_datasets_on_api.loc[match_ix]
            print("Num datasets from", provider, "on RW API:", matches.shape[0])
            return(matches)

        else:

            matches = pd.DataFrame()
            print("Not a valid provider!")
            print("Returning Empty DF")
            return(matches)


    def search_rw_api(self, search_terms = [], search_col="table_name", provider = None):
        if self.data == None:
            self.data = self.get_rw_datasets(self, provider)
        else:
            return("results")
###TO DO:
# Loop over terms
# Return a pandas dataframe
# Index = dataset name
# Cols = rw_id, table_name, table_columns
# Search the given col (cast to text to handle json) for exact matches to the search terms


# wb_datasets = pd.DataFrame([carto_data.loc[ix] for ix in carto_data.index if "wb" in carto_data.loc[ix, "table_name"]])



    def create_geojson_from_csv(self,df,lat_col="latitude",lon_col="longitude",buffer_dist=0):
        geojson_shell = {
          "type": "FeatureCollection",
          "features": []
        }
        # TO DO: add support for creating a buffer
        geojson_shell["features"] = list(map(self.add_csv_point_to_geojson, df[lon_col], df[lat_col]))
        return(geojson_shell)

    def add_csv_point_to_geojson(self, lon, lat, props=None):
        point = deepcopy(self.point_template)
        # TO DO: Add logic for passing props, if deemed necessary
        # point["properties"] = map(func, props)
        point["geometry"]["coordinates"] = [float(lon), float(lat)]
        return(point)







    def create_wkt_geom_lists(self, features, buffer_amt=0):
        point_list = []
        poly_list = []
        for feature in features:
            geom = feature["geometry"]
            geom_type = geom["type"]
            geom_coords = geom["coordinates"]
            geom_query = self.create_wkt_from_geojson(geom_type, geom_coords, buffer_amt)

            if((geom_type=="Point") & ("Buffer" not in geom_query)):
                point_list.append(geom_query)
            else:
                poly_list.append(geom_query)

        geom_lists = {
            "points":point_list,
            "polygons":poly_list
        }

        return(geom_lists)

    @staticmethod
    def create_wkt_from_geojson(geom_typ, geom_coords, buffer_amt=0):
        if geom_typ == "Point":
            point = geom_coords
            point_coords = str(point[0]) + " " + str(point[1])

            if(float(buffer_amt)>0):
                point_template = "ST_Buffer(ST_GeomFromText('POINT({})', 4326), {})"
                return(point_template.format(point_coords, buffer_amt))
            else:
                point_template = "ST_GeomFromText('POINT({})', 4326)"
                return(point_template.format(point_coords))

        elif geom_typ == "Polygon":
            geom_coords = geom_coords[0]
            poly_coords = ""
            for ix, point in enumerate(geom_coords):
                if(ix < len(geom_coords)-1):
                    poly_coords += str(point[0]) + " " + str(point[1]) + ", "
                else:
                    poly_coords += str(point[0]) + " " + str(point[1])

            if(float(buffer_amt)>0):
                poly_template = "ST_Buffer(ST_GeomFromText('POLYGON(({}))', 4326), {})"
                return(poly_template.format(poly_coords, buffer_amt))
            else:
                poly_template = "ST_GeomFromText('POLYGON(({}))', 4326)"
                return(poly_template.format(poly_coords))


    def create_wkt_union_statement(self, features):
        union_temp = "ST_Union({}, {})"
        if len(features)>1:
            union_seed = union_temp.format(features[0], self.create_wkt_union_statement(features[1:]))
            return(union_seed)
        try:
            return(features[0])
        except:
            return("No valid features")
