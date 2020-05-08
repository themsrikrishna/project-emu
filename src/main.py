from flask import Flask
from flask import request
import os.path
import requests

app = Flask(__name__)

outputDirectory = "data/"

ports = list(range(5000, 5002))


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


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        key = request.form['key']
        value = request.form['value']
        is_client = request.form['is_client']
        data = {"key": key, "value": value}
        print(data)
        result = write_file(filename=key, data=value)
        if is_client == "1":
            requests.post("http://node-2:5000", data={"key": key, "value": value, "is_client": "0"})
        return {"result": result}
    else:
        key = request.form['key']
        value = read_file(key)
        data = {"key": key, "value": value}
        print(data)
        return {"result": value}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
