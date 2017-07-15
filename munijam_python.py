from flask import Flask, render_template

from nextbus import get_vehicle_locations

app = Flask(__name__)


@app.route('/')
def hello_world():
    vehicles = get_vehicle_locations()
    return render_template('main.html', vehicles=vehicles)


if __name__ == '__main__':
    app.run(debug=True)
