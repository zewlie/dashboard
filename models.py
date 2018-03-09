"""Classes for masondash."""

from flask_sqlalchemy import SQLAlchemy

SQLALCHEMY_TRACK_MODIFICATIONS = True
db = SQLAlchemy()


class Widget(db.Model):
    """"""

    __tablename__ = "widgets"

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    type_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    size = db.Column(db.Integer, nullable=False)

    item = db.relationship("WidgetItem", backref=db.backref("items"))

    def __repr__(self):
        """Provides helpful representation when printed."""

        return "<Item id={} type={} name={}".format(self.id,
                                                    self.type_id,
                                                    self.name)

    def __init__(self, type_id, name, size):
        self.type_id = type_id
        self.name = name
        self.size = size


class WidgetItem(db.Model):
    """"""

    __tablename__ = "items"

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    widget_id = db.Column(db.Integer, db.ForeignKey('widgets.id'), nullable=False)
    text = db.Column(db.String(500))
    score = db.Column(db.Integer)
    color_class = db.Column(db.String(50))
    progress = db.Column(db.Integer)
    img_url = db.Column(db.String(300))

    def __repr__(self):
        """Provides helpful representation when printed."""

        return "<Item id={} widget_id={}".format(self.id,
                                                    self.widget_id)

    def __init__(self, widget_id, text=None, score=None, color_class=None, progress=0, img_url=None):
        self.widget_id = widget_id
        self.text = text
        self.score = score
        self.color_class = color_class
        self.progress = progress
        self.img_url = img_url
