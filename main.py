from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/admin",methods=["GET"])
def HelloWorld():
    text = "Hello world!"
    return jsonify(text)
app.run()