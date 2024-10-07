import os
from flask import Flask, render_template, url_for

app = Flask(__name__)
@app.route('/', methods = ['GET'])
def index():
    return render_template("index.html")

@app.route('/login')
def hello():
    return render_template("login.html")

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)