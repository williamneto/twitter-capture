# -*- coding: utf-8 -*-
import os
from flask import Flask, request, jsonify
import json

app = Flask(__name__)
DIR = "tweetsreader/tweets/"
@app.route("/receive_tweets", methods=["GET", "POST"])
def receive_tweets():
    tag_save_name = request.args.get("tag_save_name")

    if tag_save_name:
        if os.path.isfile("%s%s.json" % (DIR, tag_save_name)):
            with open("%s%s.json" % (DIR, tag_save_name)) as file:
                current_data = json.load(file)
        else:
            with open("%s%s.json" % (DIR, tag_save_name), "w") as file:
                current_data = []
                file.write(json.dumps(current_data))

        with open("%s%s.json" % (DIR, tag_save_name), "w") as file:
            new_data = json.loads(request.get_json()[0])
            current_data.append(new_data)

            file.write(json.dumps(current_data))
        
        return jsonify(current_data)

if __name__ == "__main__":
	app.run(debug=False, host="0.0.0.0")

# python .\twitter-capture.py -q "Forças Armadas" -t stream -u "http://127.0.0.1:5000/receive_tweets?tag_save_name=forcasarmadas" --nolog