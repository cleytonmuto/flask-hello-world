from flask import Flask

app = Flask(__name__)

@app.route("/")    
def index():
    return '<h1 style="color:blue;font-family=Arial">Hello, world!</h1>'

app.run(host='0.0.0.0', port=5000)
