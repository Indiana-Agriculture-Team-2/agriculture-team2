from flask import Flask, render_template, url_for, make_response
import os
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/sponsor')
def sponsor():
    farmers = ["David Lamb", "Michael Smith", "John Doe", "Sarah Smith", "Cole Metzger"]
    return render_template("sponsor.html", farmers=farmers)

if __name__ == '__main__':
    ##debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080))
    app.run()
    