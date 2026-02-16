from flask import Flask, render_template

app = Flask(__name__)

# Home route now renders the About page
@app.route('/')
def home():
    return render_template('about.html')

# About route (optional, you can keep it too)
@app.route('/about')
def about():
    return render_template('about.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)
