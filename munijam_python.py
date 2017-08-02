import calendar
from operator import attrgetter

from flask import Flask, render_template, jsonify

from muni_locations import get_vehicle_locations
from nextbus import parse_muni_data, get_raw_muni_data

app = Flask(__name__)


@app.route('/')
def live():
    vehicles = parse_muni_data(get_raw_muni_data())
    return render_template('main.html', vehicles=vehicles)

@app.route('/by_vehicle')
def by_vehicle():
    vehicles = parse_muni_data(get_raw_muni_data())
    return render_template('by_vehicle.html', vehicles=vehicles)


@app.route('/by_vehicle_geojson')
def by_vehicle_json():
    locations = get_vehicle_locations()
    coords = list(map(lambda x: [x["lat"], x["lon"]], locations))
    timestamps = list(map(lambda x: calendar.timegm(x['timestamp'].timetuple())*1000, locations))
    return jsonify({
          "type": "Feature",
          "geometry": {
            "type": "MultiPoint",
            "coordinates": coords
          },
          "properties": {
            "time": timestamps
          }
        })



if __name__ == '__main__':
    app.run(debug=True)
