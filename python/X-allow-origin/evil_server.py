from flask import Flask, render_template
import requests


app = Flask(__name__, static_url_path='/static', static_folder='static')

app.config['DEBUG'] = True

@app.route("/")
def start():
    return render_template("index.html")

@app.route("/allowed", methods=['GET'])
def allowed():
    content = requests.get('http://0.0.0.0:5000/allowed', timeout=60).content
    return render_template('index.html', content = content)

@app.route("/protected", methods=['GET'])
def protected():
    content = requests.get('http://0.0.0.0:5000/protected', timeout=60).content
    return render_template('index.html', content = content)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1337)
