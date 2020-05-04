from flask import Flask
from flask import request

app = Flask(__name__)

outputDirectory = "data/"


def write_file(filename, data):
    file = open(filename, "w")
    result = file.write(data)
    file.close()
    return result


def read_file(filename):
    file = open(filename, "r")
    data = file.read()
    file.close()
    return data


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        key = request.form['key']
        value = request.form['value']
        data = {"key": key, "value": value}
        print(data)
        result = write_file(filename=key, data=value)
        return {"result": result}
    else:
        key = request.form['key']
        value = read_file(key)
        data = {"key": key, "value": value}
        print(data)
        return {"result": value}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
