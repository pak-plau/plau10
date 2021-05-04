from flask import Flask, render_template
import urllib, json

app = Flask(__name__)

f = open("keys/nytimes.txt", "r")
nyt_link = "https://api.nytimes.com/svc/movies/v2/reviews/search.json?query=aocvxpoainetspoia&api-key=" + f.read()
f.close()

f = open("keys/tmdb.txt", "r")
tmdb_link = "https://api.themoviedb.org/3/search/movie?query=john%20wick&api_key=" + f.read()
f.close()

@app.route("/", methods=["GET"])
def root():
    u = urllib.request.urlopen(tmdb_link)
    data1 = json.loads(u.read())
    u = urllib.request.urlopen(nyt_link)
    data = json.loads(u.read())
    return render_template("data.html", data=data, extra=data, data1 = data1, extra1=data1["results"][0]["release_date"])

if __name__ == "__main__":
    app.debug = True
    app.run()