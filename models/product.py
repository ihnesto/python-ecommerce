from app import db

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.String(150), nullable=False)
    price = db.Column(db.Float(), nullable=False)
    discount = db.Column(db.Float())
    image = db.Column(db.String(150))

    def __repr__(self):
        return f"Product({self.desc} - {self.price})"
