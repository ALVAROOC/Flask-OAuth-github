from flask import Flask, render_template, url_for, request, redirect, make_response
from flask_dance.contrib.github import make_github_blueprint, github
import random
import json
import time



app = Flask(__name__)

app.config["SECRET_KEY"] = ""

github_blueprint = make_github_blueprint(client_id="", client_secret="")

app.register_blueprint(github_blueprint, url_prefix="/github_login")


@app.route("/")
def github_login():
    if not github.authorized:
        return redirect(url_for('github.login'))
    else:
        account_info = github.get("/user")
        if account_info.ok:
            account_info_json = account_info_json()
            return f'<h1 style="text-align:center;"> Your Github name is {account_info_json["login"]}'
    return  '<h1 style="text-align:center;">Request Failed!!!</h1>'

@app.route("/data", methods=["GET", "POST"])
def data():
    data = [time.time() * 1000, random.random() * 100]
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response


if __name__ == '__main__':
    app.run(debug=True)