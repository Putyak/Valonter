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

    data = []
    for i in streets_id:
        i = str(i)
        street_record = all_streets[i]
        data.append(street_record)
    #  Перебираю список с улицами и записаваю по ним данные

    return jsonify(data)


@app.route('/volunteers/', methods=["GET"])
def get_volunteers():
    streets = request.args.get("streets")
    with open("streets.json") as file_streets:
        data_streets = json.load(file_streets)
    street_set = data_streets[streets]
    valonter_id = street_set['volunteer']
    with open("volunteers.json") as file_volunteers:
        data_volunteer = json.load(file_volunteers)
    data = []
    for i in valonter_id:
        i = str(i)
        valonter_record = data_volunteer[i]
        data.append(valonter_record)
    return jsonify(data)


@app.route('/helpme/', methods=["POST"])
def post_helpme():
    data = flask.request.json
    with open('helpme.json', 'w') as f:
        json.dump(data, f)
    return jsonify({"status": "success"}), 201


if __name__ == '__main__':
    app.run()