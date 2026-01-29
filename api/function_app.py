
#import azure.functions as func
import random
from flask import Flask, jsonify
from flask_cors import CORS # type: ignore

app = Flask (__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "Hello, World. This is a test!!!!"

@app.route("/about")
def about():
    return "We are over 1000 members and fastest growing platform. \n"    "Our community is expanding at an unprecedented rate, and we are proud to announce that we have officially surpassed 1,000 active members"

@app.route("/contact")
def contact():
    return "You can contact us on nnour@imudsolutions."

@app.route ("/random")
def get_random():
    number = random.randint (1, 1000)
    return jsonify({"number": number}) 

if __name__ == "__main__":
    app.run(debug=True, port=5000)

  #  app = func.WsgiFunctionApp(
  #  app=flask_app.wsgi_app, 
  #  http_auth_level=func.AuthLevel.ANONYMOUS
#)