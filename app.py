from flask import Flask, render_template, request, redirect
import csv
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

def store_data_in_csv(data):
    email = data["email"]
    subject = data["subject"]
    message = data["message"]
    with open('database.csv', mode='a', newline='') as database1:
        write = csv.writer(database1)
        write.writerow([email, subject, message])


@app.route("/submit_form", methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        store_data(data)
        store_data_in_csv(data)
        return redirect('./thankyou.html')
    else:
        return "Something went wrong !!"

# @app.route("/index.html")
# def home():
#     return render_template('index.html')

# @app.route("/works.html")
# def works():
#     return render_template('works.html')

# @app.route("/work.html")
# def work():
#     return render_template('work.html')

# @app.route("/about.html")
# def about():
#     return render_template('about.html')

# @app.route("/contact.html")
# def contact():
#     return render_template('contact.html')

# @app.route("/components.html")
# def componenets():
#     return render_template('components.html')
