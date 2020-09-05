from dataclasses import dataclass

@dataclass
class MapboxInfo:
    prefix: str = "https://api.mapbox.com/directions-matrix/v1/mapbox/"
    profile: str = "driving"
    access_token: str = "pk.eyJ1IjoiYXM0Njg1NzkiLCJhIjoiY2tkcjJscDkzMWJobTJzbWgyZWpsbDl4cyJ9.03T640DTC8fhKTBZ4lVQxw"