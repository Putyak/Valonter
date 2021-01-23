import json
import flask
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/districts/', methods=["GET"])
def get_all_districts():
    with open("districts.json") as f:
        districts = json.load(f)

    data = []
    for i, j in districts.items():
        d_data = {
        "id": i,
        "title": j['title'],
    }
        data.append(d_data)

    return flask.jsonify(data)


@app.route('/streets/', methods=["GET"])
def get_streets():
    district = request.args.get("district")
    # Получение значение искомого района из запроса
    with open("districts.json") as file_districts:
        data_districts = json.load(file_districts)
    # Открытие файла с списком районов и запись их в переменную
    streets_data = data_districts[district]
    # Получение искомого района в фале
    streets_id = streets_data['streets']
    # Получение массива улиц, которые надо найти
    with open("streets.json") as file_streets:
        all_streets = json.load(file_streets)
    # Получение файла с списком улиц и запись их в переменную


    data=[]
    for i, j in all_streets.items():
        for f in streets_id:
            if int(f) == int(i):
                s_data = {
            "id": i,
            "title": j['title'],
            "volunteer": j['volunteer']
                }
                data.append(s_data)


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
    for i, j in data_volunteer.items():
        for f in valonter_id:
            if int(f) == int(i):
                v_data = {
                    "id": i,
                    "name": j['name'],
                    "userpic": j['userpic'],
                    "phone": j['phone']
                }
                data.append(v_data)
    return jsonify(data)


@app.route('/helpme/', methods=["POST"])
def post_helpme():
    data = flask.request.json
    with open('helpme.json', 'w') as f:
        json.dump(data, f)
    return jsonify({"status": "success"}), 201


if __name__ == '__main__':
    app.run()