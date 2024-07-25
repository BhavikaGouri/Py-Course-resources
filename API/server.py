import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hey():
    return "<h1>Write the name in the URL route</h1>"


@app.route("/<Name>")
def home(Name):
    URL_GENDER = f"https://api.genderize.io?name={Name}"
    URL_AGE = f"https://api.agify.io?name={Name}"

    data = requests.get(URL_GENDER)
    data2 = requests.get(URL_AGE)

    list1 = data2.text.replace("}", "").split(":")
    age = int(list1[3])

    data_dict = data.text
    gender = ""
    if "female" in data_dict:
        gender = "Female"
    else:
        gender = "Male"
    return render_template("index.html", name=Name, Age=age, Gender=gender)


if __name__ == "__main__":
    app.run(debug=True)
