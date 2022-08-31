from flask import Flask, render_template
import datetime
import requests


CURRENT_YEAR = datetime.date.today().year
YOUR_NAME = "Dawid"



app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", kto_zrobił=YOUR_NAME, rok = CURRENT_YEAR)

@app.route("/guess/<user_name>")
def name_and_gender(user_name):

    age_response = requests.get(f"https://api.agify.io?name={user_name}")
    gender_response = requests.get(f"https://api.genderize.io?name={user_name}")
    age = age_response.json()["age"]
    gender = gender_response.json()["gender"]
    return render_template("guess.html", imie=user_name, plec=gender, wiek=age)


@app.route("/blog/<num>")
def get_blog(num):
    blog_url = "https://api.npoint.io/b06b99ae65204771b5eb"
    response = requests.get(blog_url)
    all_posts = response.json()
    print(all_posts)
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run()