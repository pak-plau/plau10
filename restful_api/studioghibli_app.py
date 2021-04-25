from flask import Flask, render_template
import urllib, json

app = Flask(__name__)

link = 'https://ghibliapi.herokuapp.com/films?title=My%20Neighbor%20Totoro'

@app.route("/", methods=["GET"])
def root():
    u = urllib.request.urlopen(link)
    data = json.loads(u.read())
    return render_template("data.html", data=data)

if __name__ == "__main__":
    app.debug = True
    app.run()