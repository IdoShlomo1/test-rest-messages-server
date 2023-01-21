#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, jsonify, request
from validators import MessageValidator
app = Flask(__name__)

db = []


def get_message_by_attr(key, value):
    if key in MessageValidator.ATTRIBUTES:
        return [record for record in db if record[key] == value]
    return None


def _convert_format(key, value):
    if key == 'application':
        value = int(value)
    elif key == 'participants':
        value = json.loads(value)
    return value


@app.route('/api/AddMessage', methods=['POST'])
def create_message():
    record = json.loads(request.data)
    if not MessageValidator.is_message_valid(record):
        return jsonify({"Error": "Records data is not valid"}), 400

    if get_message_by_attr('message_id', record.get('message_id')):
        return jsonify({"Error": "Record already exists"}), 400

    db.append(record)
    return jsonify({"Record Added": record})


@app.route('/api/GetMessages', methods=['GET'])
def get_messages():
    search_key = dict(request.args)
    if not search_key:
        return jsonify(db)
    else:
        key, value = list(search_key.items())[0]
        value = _convert_format(key, value)
        records = get_message_by_attr(key=key, value=value)
        if records:
            return jsonify(records)

    return jsonify({"Error": "Record does not exist"}), 404


@app.route('/api/DeleteMessage', methods=['DELETE'])
def delete_message():
    search_key = dict(request.args)
    key, value = list(search_key.items())[0]
    # if key == 'application':
    #     value = int(value)
    # if key == 'participants':
    #     value = json.loads(value)
    value = _convert_format(key, value)

    records = get_message_by_attr(key=key, value=value)
    if records:
        for record in records:
            db.remove(record)

        return jsonify({"Records Deleted": len(records)})

    return jsonify({"Error": "Record does not exist"}), 404


if __name__ == '__main__':
    # app.run()
    app.run(debug=True)
