from app import app, db
from routes.index import index
from routes.register import register
from routes.login import login
# from models.product import Product


if __name__ == '__main__' :
    app.run(debug=True)


# def insertDataToDB():
#     p = ['Product name goes here just for demo item', 1280, "/static/images/main-page/" ]

#     for i in range(1, 10) :
#         prod = Product(desc=p[0], price=p[1], image=f'{p[2]}{i}.jpg')
#         db.session.add(prod)
#         db.session.commit()
