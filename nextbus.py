import xml.etree.ElementTree as ET
from collections import namedtuple

import requests

MUNI_METRO_ROUTES = frozenset(["N", "M", "L", "KT", "J"])
Vehicle = namedtuple("Vehicle", "lat lon route_tag")

def parse_muni_data(api_response):

    vehicles = ET.fromstring(api_response).getchildren()
    vehicles = [
        v for v in vehicles
        if v.attrib.get('routeTag') in MUNI_METRO_ROUTES
    ]
    filtered_vehicles = [
        Vehicle(v.attrib['lat'], v.attrib['lon'], v.attrib['routeTag'])
        for v in vehicles
        if 'lat' in v.attrib and 'lon' in v.attrib
    ]
    return filtered_vehicles

def get_raw_muni_data():
    return requests.get("http://webservices.nextbus.com/service/publicXMLFeed?command=vehicleLocations&a=sf-muni&t=0").text

if __name__ == "__main__":
    locs = parse_muni_data(get_raw_muni_data())
    print(locs)