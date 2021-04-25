from flask import Flask, render_template
import urllib, json

app = Flask(__name__)

f = open("keys/tmdb.txt", "r")
link = "https://api.themoviedb.org/3/discover/movie?with_genres=28&page=2&api_key=" + f.read()
f.close()

@app.route("/", methods=["GET"])
def root():
    u = urllib.request.urlopen(link)
    data = json.loads(u.read())
    return render_template("data.html", data=data)

if __name__ == "__main__":
    app.debug = True
    app.run()