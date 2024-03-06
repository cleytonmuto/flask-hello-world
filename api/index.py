from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/<page>")   
def index(page):
    # return '<h1 style="color:blue;font-family=Arial">Hello, world!</h1>', 200
    return f'<h1 style="color:red;font-family=Arial">Certificado ABCD000{page}!</h1>', 200


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"status": 404, "message": "Not Found"}), 404
