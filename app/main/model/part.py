from .. import db

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Part(db.Model):
    """ Part Model for storing Dieform parts info """
    __tablename__ = "part"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_id = db.Column(db.Integer, ForeignKey('customer.id'))
    purchase_order_id = db.Column(db.Integer, ForeignKey('purchase_order.id'))
    number = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)

    receivedParts = relationship("ReceivedPart")

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        return "<Part number: '{}'>".format(self.number)