from flask import Flask, render_template, url_for, make_response
import os
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

class Farmer:
    def __init__(self, farmName, location, products, delivery):
        self.farmName = farmName
        self.location = location
        self.products = products
        self.delivery = delivery

## Example Farmer Data
farmers = ["David Lamb", "Michael Smith", "John Doe", "Sarah Smith", "Joe Brown", "Emma Johnson"]
farmNames = ["Boulder Valley Lands", "Bull's Eye Farms", "Black Raven Farm", "Meadowland Pastures", "Robinwood Estate", "Stallion Estate"]
locations = ["Lebonon, IN", "Carmel, IN", "Fort Wayne, IN", "Bluffton, IN", "Bloominton, IN", "Greenfield, IN"]
products = [["Tomatoes"], ["Corn", "Soybeans"], ["Corn"], ["Squash", "Tomatoes"], ["Carrots", "Squash", "Tomatoes"], ["Soybeans"]]
delivery = [True, True, False, True, False, False]

@app.route('/sponsor')
def sponsor():
    return render_template("sponsor.html", farmers=farmers, farmNames=farmNames, locations=locations, products=products, delivery=delivery)


@app.route('/checkout/<name>/')
def checkout(name):
    return render_template("checkout.html", name=name)

if __name__ == '__main__':
    ##debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080))
    app.run()
    