from flask import Flask
from src.logger import logging
from src.exception import CustomException
import sys
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return "Consignment Price Preditction"

if __name__ == "__main__":
    app.run(debug=True)


