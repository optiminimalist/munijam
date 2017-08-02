import xml.etree.ElementTree as ET
from collections import namedtuple

import requests

MUNI_METRO_ROUTES = frozenset(["N", "M", "L", "KT", "J"])
Vehicle = namedtuple("Vehicle", "lat lon route_tag vehicle_id direction_tag secs_since_report heading speed")


def parse_muni_data(api_response):
    vehicles = ET.fromstring(api_response).getchildren()
    vehicles = [
        v for v in vehicles
        if v.attrib.get('routeTag') in MUNI_METRO_ROUTES
    ]
    filtered_vehicles = [
        Vehicle(v.attrib['lat'], v.attrib['lon'], v.attrib.get('routeTag'), v.attrib['id'], v.attrib.get('dirTag'), v.attrib.get('secsSinceReport'), v.attrib.get('heading'), v.attrib.get('speedKmHr'))
        for v in vehicles
        if 'lat' in v.attrib and 'lon' in v.attrib
    ]

    return filtered_vehicles


def get_raw_muni_data():
    return requests.get("http://webservices.nextbus.com/service/publicXMLFeed?command=vehicleLocations&a=sf-muni&t=0&r=N").text

