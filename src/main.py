from flask import Flask
from flask import request
import os.path
import requests

app = Flask(__name__)

outputDirectory = "data/"

NODES = os.getenv('EMU_NODES')
PORT = os.getenv('EMU_PORT')
NODE = os.getenv('EMU_NODE')


def write_file(filename, data):
    filepath = os.path.join(outputDirectory, filename)
    file = open(filepath, "w")
    result = file.write(data)
    file.close()
    return result


def read_file(filename):
    filepath = os.path.join(outputDirectory, filename)
    file = open(filepath, "r")
    data = file.read()
    file.close()
    return data


@app.route('/write', methods=['POST'])
def write_file_route():
    key = request.form['key']
    value = request.form['value']
    result = write_file(filename=key, data=value)
    print(NODE)
    return {"result": result}


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        key = request.form['key']
        value = request.form['value']
        result = write_file(filename=key, data=value)
        print(NODE)
        for node in range(1, int(NODES)+1):
            if node != int(NODE):
                requests.post('http://node-{0}:{1}/write'.format(node, PORT), data={"key": key, "value": value})
        return {"result": result}
    else:
        key = request.form['key']
        value = read_file(key)
        data = {"key": key, "value": value}
        return {"result": value}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
