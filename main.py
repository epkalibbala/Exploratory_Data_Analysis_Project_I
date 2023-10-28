from flask import Flask, render_template
import requests
import json

app = Flask(__name__)


@app.route('/')
def home():
    url = f"https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url)
    # print(response.json())
    data = response.json()
    return render_template("index.html", resp=data)


if __name__ == "__main__":
    app.run(debug=True)
