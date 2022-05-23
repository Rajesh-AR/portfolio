from flask import Flask, render_template, request, redirect
import csv
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

@app.route("/")
def universe():
    return render_template('index.html')

@app.route("/<string:page_name>")
def random_pages(page_name):
    return render_template(page_name)

def store_data(data):
    email = data["email"]
    subject = data["subject"]
    message = data["message"]
    with open('database.txt', mode='a') as databse:
        file = databse.write(f"\n{email}, {subject}, {message}")

def send_email_confirmation(name, email_id):
    email = EmailMessage()
    email['from'] = 'Rajesh Arya'
    email['to'] = email_id
    email['subject'] = 'Contact form has been submitted !!'

    email.set_content(f'Hi {name},\n\nYour contact request has been submitted and confirmed. We will get back to you as soon as possible.\nThis is an automated email, so please do not reply on this email.\n\n Regards,\n Rajesh Arya\n Python Developer ')

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('rajesh.arya.py@gmail.com', 'Imra@111')
        smtp.send_message(email)

def store_data_in_csv(data):
    name = data["name"]
    email = data["email"]
    subject = data["subject"]
    message = data["message"]
    with open('database.csv', mode='a', newline='') as database1:
        write = csv.writer(database1)
        write.writerow([name, email, subject, message])
    send_email_confirmation(name, email)


@app.route("/submit_form", methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        store_data(data)
        store_data_in_csv(data)
        return redirect('./thankyou.html')
    else:
        return "Something went wrong !!"
