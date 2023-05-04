from flask import Flask
from housing.logger import logging
from housing.exception import HousingException
import sys
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    try:
        raise Exception("CUSTOM EXCEPTION")
    except Exception as ex:
        housing =  HousingException(ex,sys)
        logging.info(housing.error_message)
        logging.info("TESTING")
    return "Consignment Price Preditction"

if __name__ == "__main__":
    app.run(debug=True)


