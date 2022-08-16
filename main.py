from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello_world():
    title = "Bohao's page"
    return render_template('index.html', title=title)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug='False', port='8080')