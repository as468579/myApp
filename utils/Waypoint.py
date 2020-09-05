from dataclasses import dataclass

@dataclass
class Waypoint:
    latitude: float
    longitude: float
    stayTime: float