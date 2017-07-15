from flask import Flask, render_template

from nextbus import parse_muni_data, get_raw_muni_data

app = Flask(__name__)


@app.route('/')
def hello_world():
    vehicles = parse_muni_data(get_raw_muni_data())
    return render_template('main.html', vehicles=vehicles)


if __name__ == '__main__':
    app.run(debug=True)
