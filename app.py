from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index() :
  return render_template("index.html")



@app.route("/home")
def home() :
  return render_template("home.html")

@app.route('/artists')
def artists():
  return render_template("artists.html")

@app.route('/playlists')
def playlists():
  return render_template("playlists.html")

@app.route('/settings')
def settings():
  return render_template("settings.html")
    

if __name__ == "__main__":
  app.run(host = '0.0.0.0', debug = True)

