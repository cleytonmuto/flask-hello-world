from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")   
def index():
    return '<h1 style="color:blue;font-family=Arial">Hello, world!</h1>', 200

for hash in range(1,5):
    @app.route("/ABCD000" + hash)
    def index():
        return f'<h1 style="color:blue;font-family=Arial">Hello, world {hash}!</h1>', 200

app.errorhandler(404)
def page_not_found(e):
    return jsonify({"status": 404, "message": "Not Found"}), 404

