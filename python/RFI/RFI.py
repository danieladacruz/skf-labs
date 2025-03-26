from flask import Flask, request, render_template
import datetime
import os
from urllib.parse import urlparse
from security import safe_requests

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/")
def start():
    return render_template("index.html")


@app.route("/cmd", methods=['POST'])
def cmd():
    filename = request.form['filename']
    try:
        if "http" not in str(urlparse(filename).scheme):
            host = request.url[:-4]
            filename = host+"/static/" + filename
            result = eval(safe_requests.get(filename).text)
            return render_template("index.html", result=result)
        else:
            result = eval(safe_requests.get(filename).text)
            return render_template("index.html", result=result)
    except Exception:
        return render_template("index.html", result="Unexpected error during the execution of the predefined command.")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', threaded=True)
