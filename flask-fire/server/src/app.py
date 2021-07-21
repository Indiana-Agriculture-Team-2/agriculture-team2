from flask import Flask, render_template, url_for, request
import os

UPLOAD_FOLDER = "C:/Users/colej/OneDrive/Documents/SOSChallenge_2021/agriculture-team2/flask-fire/server/src/static"
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

## Starter Farmer Data
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

## Starter social media post data
postData = [["These strawberry seeds are fresh, ripe, and juicy! Order strawberry seeds online. Don't miss out!", "David Lamb"], ["Watermelon in season now! Save 20% on watermelon seeds!", "Michael Smith"]]

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
    if request.method == "POST":
        ######FILE UPLOAD#########
        ##Used https://stackoverflow.com/questions/44926465/upload-image-in-flask for code in between commments
        if 'file' not in request.files:
            return 'there is no file in form!'
        file = request.files['file']
        path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(path)
        filename = file.filename
        print(file)
        ######FILE UPLOAD#########

        ##TEXT AND DATA STRUCTURE UPDATE##
        newPost = request.form["nm"]
        newPostUser = "New User" ##Temporary as we don't have accounts functional yet.
        if file != "":
            postData.append([newPost, newPostUser, filename])
        else:
            postData.append([newPost, newPostUser])
        print(postData)
        ##RENDER TEMPLATE##
        return render_template("social.html", postData=postData)
    else:
        return render_template("social.html", postData=postData)

if __name__ == '__main__':
    ##debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080))
    app.run()
    