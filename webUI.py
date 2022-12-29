import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    with open('database.json', 'r') as f:
        data = json.load(f)
    return render_template('./index.html', data=data,)

with open('database.json', 'r') as f:
        data = json.load(f)

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=8000)

