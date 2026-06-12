from flask import Flask, render_template
import data_manager
import api_service

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/events")
def events():
    data = data_manager.get_events()
    return render_template("index.html", category="events", title="🎭 Evente Kulturore", data=data)

@app.route("/tourism")
def tourism():
    data = data_manager.get_tourism()
    return render_template("index.html", category="tourism", title="🏛️ Destinacione Turistike", data=data)

@app.route("/restaurants")
def restaurants():
    data = data_manager.get_restaurants()
    return render_template("index.html", category="restaurants", title="🍕 Restorante dhe Bare", data=data)

@app.route("/emergency")
def emergency():
    data = data_manager.get_emergency()
    return render_template("index.html", category="emergency", title="🚨 Shërbime Urgjence", data=data)

@app.route("/embassies")
def embassies():
    data = data_manager.get_embassies()
    return render_template("index.html", category="embassies", title="🏳️ Ambasadat", data=data)

@app.route("/weather")
def weather():
    data = api_service.get_weather()
    return render_template("index.html", category="weather", title="🌤️ Moti i Tiranës", data=data)

if __name__ == "__main__":
    app.run(debug=True)