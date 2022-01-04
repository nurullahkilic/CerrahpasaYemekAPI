import requests
from flask import Flask, jsonify
import json
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/')
def hello():

    # Cerrahpaşa API Endpoint Options
    siteKey = "C9C078A3C4214BBE91E6014335636C3B"
    EID = "4E00590053005F006D004C00500035005500720059003100"
    api_adress = "https://service-cms.istanbulc.edu.tr/api/webclient/f_getData?siteKey={}&EID={}".format(
        siteKey, EID)

    # Get data from api
    data = requests.get(api_adress)
    res = json.loads(data.json()["Data"])

    # Create empty list for items
    FOODS = []
    for key in res["ogle"]:

        date = key['tarih']
        calorie = key['kalori']
        menu = key['menu'].split("\t\n")  # Split the foods
        menu = list(
            map(lambda x: x.strip(), menu))  # Delete the spaces

        # Create JSON object for each day
        items = {
            "date": date,
            "calorie": calorie,
            "menu": menu
        }

        # Append every single day in for loop
        FOODS.append(items)
    return jsonify(FOODS)


if __name__ == "__main__":
    app.run(debug=True)
