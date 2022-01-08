from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    app.route('/')
    return render_template("index.html")


@app.route('/projects/')
def projects():
    return render_template("projects.html")


@app.route('/contact/')
def contact():
    return render_template("contact.html")

@app.route('/github/')
def github():
    return render_template("github.html")

@app.route('/blog/')
def blog():
    return render_template("blog.html")

@app.route('/linkedin/')
def linkedin():
    return render_template("linkedin.html")

@app.route('/privacypolicy/')
def privacypolicy():
    return render_template("privacypolicy.html")

@app.route('/resume/')
def resume():
    return render_template("caseyandhastings.jpg")

@app.route('/form-to-email.php/')
def formtoemail():
    return render_template("form-to-email.php")

if __name__ == "__main__":
    app.run(debug=True)
