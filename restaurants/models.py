from restaurant import app, db


class Restaurant_name(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    user = db.Column(db.String(80), nullable=False)

    def __init__(self, name, user):
        self.name = name
        self.user = user

    def __repr__(self):
        return '<Restaurant %r>' % self.name
