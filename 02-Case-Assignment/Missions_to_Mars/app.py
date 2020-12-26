from flask import Flask, render_template, redirect 
import pymongo
from flask_pymongo import PyMongo
import scrape_mars

#%%

app = Flask(__name__)

#%%

conn = "mongodb://localhost:27017/mars_data"
client = pymongo.MongoClient(conn)
db = client.mars_data

#%%

@app.route("/")
def index():
    facts = db.news.find_one()
    hemispheres = list(db.hemispheres.find())
    return render_template("index.html", facts=facts, hemispheres=hemispheres)

#%%

@app.route("/scrape")
def scraper():
    news = db.news
    news_data = scrape_mars.scrape()
    news.update({}, news_data, upsert=True)
    return redirect("/", code=302)
   
 #%%
if __name__ == "__main__":
    app.run(debug=True)

#%%   
   
