from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    app.route('/')
    return render_template("home.html")

@app.route('/portfolio/')
def portfolio():
    return render_template("portfolio.html")

@app.route('/contact/')
def contact():
    return render_template("contact.html")

@app.route('/privacypolicy/')
def privacypolicy():
    return render_template("privacypolicy.html")

@app.route('/resume/')
def resume():
    return render_template("caseyandhastings.jpg")

if __name__ == "__main__":
    app.run(debug=True)


# reminder -- run {flask run} in terminal to test locally
