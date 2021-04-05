from flask import Flask, render_template
import urllib, json

app = Flask(__name__)

f = open("key_nasa.txt", "r")
link = "https://api.nasa.gov/planetary/apod?api_key=" + f.read()
f.close()

@app.route("/", methods=["GET", "POST"])
def root():
    u = urllib.request.urlopen(link)
    data = json.loads(u.read())
    return render_template("main.html", image=data["url"])

if __name__ == "__main__":
    app.debug = True
    app.run()