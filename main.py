from flask import Flask, render_template, url_for
import config

app = Flask(__name__)

@app.route('/')
def index() :
    return render_template('main-page/page-listing-grid.html')

if __name__ == '__main__' :
    app.run(debug=True)
