from flask import Flask ,request, jsonify, redirect, Response, render_template
from flask_mail import Mail, Message

import os
# port = int(os.environ.get("PORT", 5002))

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

app.config["MAIL_SERVER"] = "smtp.mail.yahoo.com"
app.config["MAIL_PORT"] = 465
# app.config["MAIL_PORT"] = 587


# app.config["MAIL_USERNAME"] = "XXXXX@yahoo.com"
# app.config["MAIL_PASSWORD"] = "login to https://login.yahoo.com/myaccount/security/ to generate(not your password"

app.config["MAIL_USERNAME"] = os.getenv("Email_User")
app.config["MAIL_PASSWORD"] = os.getenv("Email_Password")
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USE_SSL"] = True

# Flask mail
mail = Mail(app)


@app.route("/")
def hello_world():
    return render_template("index.html")
    # return render_template("testEmail.html")

#  Forget and Reset password

@app.route("/email", methods=["POST"])
def test_email():
    if request.method =="POST":
        form_data = request.form.to_dict() #if the value doesnt exist, it will return a empty dict {}
        if form_data ==  {}:
            request_payload = request.json 
        else:
            request_payload = form_data


        userEmail = request_payload['email']     
        subject = "It is a test email"
        # msg = f"Hello! It is a test email and sent to you email address: {userEmail}"

        # resetMessage = Message(subject,sender="XXXXX@yahoo.com", recipients=[userEmail])

        resetMessage = Message(subject,sender=os.getenv("Email_User"), recipients=[userEmail])
        # resetMessage.body = msg
        # resetMessage.body cannot simultaneously exist
        resetMessage.html = render_template("testEmail.html")

        mail.send(resetMessage)
        success = "Message sent"



        
        return success

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5001)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT",5001)))