from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)

app.config.from_object(config.EcommerceConfig)

db = SQLAlchemy(app)


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.String(150), nullable=False)
    price = db.Column(db.Float(), nullable=False)
    discount = db.Column(db.Float())
    image = db.Column(db.String(150))

    def __repr__(self):
        return f"Product({self.desc} - {self.price})"

@app.route('/')
def index() :
    products = Product.query.all()
    return render_template('main-page/page-listing-grid.html', products=products)

if __name__ == '__main__' :
    app.run(debug=True)


# def inserDataToDB():
#     p = ['Product name goes here just for demo item', 1280, "/static/images/main-page/" ]

#     for i in range(1, 10) :
#         prod = Product(desc=p[0], price=p[1], image=f'{p[2]}{i}.jpg')
#         db.session.add(prod)
#         db.session.commit()