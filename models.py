from app import db

shops_malls = db.Table('shops_malls',
                     db.Column('shop_id', db.Integer, db.ForeignKey('shop.id', ondelete='SET NULL'), nullable=True),
                     db.Column('mall_id', db.Integer, db.ForeignKey('mall.id', ondelete='SET NULL'), nullable=True)
                     )


class Shop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Type = db.Column(db.String(140))
    Name = db.Column(db.String(140), unique=True)

    malls = db.relationship('Mall',
                            secondary=shops_malls,
                            backref=db.backref(
                                'shops',
                                lazy='dynamic',
                                )
                            )

    def __repr__(self):
        return f'< {self.Name} >'


class Mall(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100), unique=True)
    City = db.Column(db.String(100))
    District = db.Column(db.String(100))

    def __repr__(self):
        return f'< {self.Name} >'
