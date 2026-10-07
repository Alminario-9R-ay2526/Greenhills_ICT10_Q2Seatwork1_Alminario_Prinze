from flask import Flask, render_template, request

app = Flask(__name__)

# Country nicknames for Southeast Asia
COUNTRY_NICKNAMES = {
    "Brunei": "The Abode of Peace",
    "Cambodia": "The Kingdom of Wonder",
    "Indonesia": "The Emerald of the Equator",
    "Laos": "The Land of a Million Elephants",
    "Malaysia": "Truly Asia",
    "Myanmar": "The Golden Land",
    "Philippines": "The Pearl of the Orient Seas",
    "Singapore": "The Lion City",
    "Thailand": "The Land of Smiles",
    "Timor-Leste": "The Land of the Rising Sun"
}


@app.route("/", methods=["GET", "POST"])
def home():
    nickname = None
    selected_country = None

    if request.method == "POST":
        selected_country = request.form.get("country")

        # Look up the nickname of the selected country.
        nickname = COUNTRY_NICKNAMES.get(selected_country)

    return render_template(
        "index.html",
        countries=COUNTRY_NICKNAMES.keys(),
        selected_country=selected_country,
        nickname=nickname
    )


if __name__ == "__main__":
    app.run(debug=True)