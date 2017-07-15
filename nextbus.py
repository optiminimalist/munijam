import xml.etree.ElementTree as ET
from collections import namedtuple

import requests

MUNI_METRO_ROUTES = frozenset(["N", "M", "L", "KT", "J"])
Vehicle = namedtuple("Vehicle", "lat lon")

def get_vehicle_locations():
    vehicles = ET.fromstring(requests.get("http://webservices.nextbus.com/service/publicXMLFeed?command=vehicleLocations&a=sf-muni&t=0").text).getchildren()
    vehicles = [
        v for v in vehicles
        if v.attrib.get('routeTag') in MUNI_METRO_ROUTES
    ]
    filtered_vehicles = [
        Vehicle(v.attrib['lat'], v.attrib['lon'])
        for v in vehicles
        if 'lat' in v.attrib and 'lon' in v.attrib
    ]
    return filtered_vehicles

if __name__ == "__main__":
    locs = get_vehicle_locations()
    print(locs)