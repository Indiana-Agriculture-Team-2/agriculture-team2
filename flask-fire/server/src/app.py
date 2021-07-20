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
productsList = ["Corn", "Soybeans", "Squash", "Carrots", "Tomatoes"]
products = [["Tomatoes"], ["Corn", "Soybeans"], ["Corn"], ["Squash", "Tomatoes"], ["Carrots", "Squash", "Tomatoes"], ["Soybeans"]]
delivery = [True, True, False, True, False, False]

## List of states
states = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado",
  "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
  "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]

@app.route('/sponsor')
def sponsor():
    return render_template("sponsor.html", farmers=farmers, farmNames=farmNames, locations=locations, products=products, delivery=delivery)

@app.route('/accountcreation')
def accountcreation():
    return render_template("accountcreation.html", states=states, productsList=productsList)

@app.route('/checkout/<name>/')
def checkout(name):
    return render_template("checkout.html", name=name)

@app.route('/complete')
def complete():
    return render_template("complete.html")

@app.route('/social', methods=["GET", "POST"])
def social():
    return render_template("social.html")

if __name__ == '__main__':
    ##debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080))
    app.run()
    