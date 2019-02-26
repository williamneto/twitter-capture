from flask import Flask

app = Flask(__name__)

@app.route("/receive_tweets", methods=["POST"])
def receive_tweets():
    import pdb; pdb.set_trace()

if __name__ == "__main__":
	app.run(debug=False, host="0.0.0.0")