from flask import Flask, render_template, request
import requests
import smtplib

API_URL = "https://api.npoint.io/4c47f0e10a593ebaab57"
#todo fill the email and pass below
MY_MAIL = "Fill email adress here"
MY_MAIL_PASS = "Fill psw from email here"

response = requests.get(API_URL)
all_post = response.json()

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("index.html", all_post=all_post)


@app.route("/contact", methods=["GET", "POST"])
def contact_page():
    if request.method == "POST":
        send_mail(request.form["name"], request.form["email"], request.form["phone"], request.form["message"])
        return render_template("contact.html", msg_send=True)
    else:
        return render_template("contact.html", msg_send=False)


@app.route("/about")
def about_page():
    return render_template("about.html")


@app.route("/post/<int:post_id>")
def show_post(post_id):
    return render_template("post.html", post=all_post[post_id - 1])


def send_mail(name, email, phone, msg):
    email_msg = f"Subject:New message from blog site/n/nName: {name}/nEmail: {email}/nPhone number: {phone}/nMessage: {msg}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_MAIL, MY_MAIL_PASS)
        connection.sendmail(MY_MAIL, MY_MAIL, email_msg)


if __name__ == "__main__":
    app.run(debug=True)
