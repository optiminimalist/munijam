from db import conn
import os

from nextbus import parse_muni_data
from shapely import wkt
import sys
def load_muni_locations():
    files = os.listdir("../munipings")
    for f in files:
        timestamp, _ = f.split(".")
        content = open("../munipings/" + f, 'r').read()
        try:
            parsed_data = parse_muni_data(content)
            for vehicle in parsed_data:
                cur = conn.cursor()
                cur.execute("INSERT INTO muni_locations VALUES (%i, to_timestamp(%i), '%s', '%s', ST_GeographyFromText('SRID=4326;POINT(%f %f)'), %i, %i, %i)" % (
                    int(vehicle.vehicle_id),
                    int(timestamp),
                    vehicle.route_tag,
                    vehicle.direction_tag,
                    float(vehicle.lon),
                    float(vehicle.lat),
                    int(vehicle.heading),
                    int(vehicle.speed),
                    int(vehicle.secs_since_report)
                ))
                conn.commit()
        except Exception as e:
            print(e)
            print("Broken file: %s" % timestamp)

def get_vehicle_locations():
    cur = conn.cursor()
    cur.execute("SELECT ts, ST_AsText(geom) FROM muni_locations WHERE vehicle_id=1486 ORDER BY ts ASC")
    rows = cur.fetchall()

    return [
        {
            "timestamp": row[0],
            "geom": wkt.loads(row[1]),
            "lat": wkt.loads(row[1]).coords[0][0],
            "lon": wkt.loads(row[1]).coords[0][1],
        }
        for row in rows
    ]
        # print(wkt.loads(row[0]).latitude)

if __name__ == "__main__":
    load_muni_locations()