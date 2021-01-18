import json
import flask
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/districts/', methods=["GET"])
def get_all_districts():
    with open("districts.json") as f:
        districts = json.load(f)
    return flask.jsonify(districts)


@app.route('/streets/', methods=["GET"])
def get_streets():
    district = request.args.get("district")
    # Получение значение искомого района из запроса
    with open("districts.json") as f:
        data_districts = json.load(f)
    # Открытие файла с списком районов и запись их в переменную
    streets_data = data_districts[district]
    # Получение искомого района в фале
    streets_id = streets_data['streets']
    # Получение массива улиц, которые надо найти
    with open("streets.json") as f:
        all_streets = json.load(f)
    # Получение файла с списком улиц и запись их в переменную

    street_list = []
    for i in streets_id:
        for each_street in all_streets:
            if each_street[0] == i:
                street_list.append(each_street)
    # Пытаюсь пройти по всем улицам и записать их в новый массив

    return jsonify(street_list)


@app.route('/volunteers/', methods=["GET"])
def get_volunteers():
    streets = request.args.get("streets")
    with open("streets.json") as f:
        data_streets = json.load(f)
    street_set = data_streets[streets]
    valonter_id = street_set['volunteer']
    return jsonify(valonter_id)


@app.route('/helpme/', methods=["POST"])
def post_helpme():
    data = flask.request.json
    with open('helpme.json', 'w') as f:
        json.dump(data, f)
    return jsonify({"status": "success"}), 201


if __name__ == '__main__':
    app.run()