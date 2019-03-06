# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route("/receive_tweets", methods=["GET", "POST"])
def receive_tweets():
    with open("tuiutinotazero.json") as file:
        current_data = json.load(file)

    with open("tuiutinotazero.json", "w") as file:
        new_data = json.loads(request.get_json()[0])
        current_data.append(new_data)

        file.write(json.dumps(current_data))
    
    return jsonify(current_data)

if __name__ == "__main__":
	app.run(debug=False, host="0.0.0.0")