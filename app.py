from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mission_to_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/weather_app")


# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    destination_data = mongo.db.collection.find_one()

    # get data from scrape_costa
    scraped_data = mission_to_mars.scrape_news()
    scraped_f_img = mission_to_mars.scrape_f_image()
    scrape_tweet = mission_to_mars.scrape_tweet() 
    scrape_hem_images = mission_to_mars.scrape_images()
    scrape_table = mission_to_mars.scrape_table()
    # Return template and data
    return render_template("index.html", mars=scraped_data, f_image=scraped_f_img, w_tweet=scrape_tweet, h_images=scrape_hem_images, m_table=scrape_table)

# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function
    mars_dict = mission_to_mars.scrape_info()

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, scraped_data, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
