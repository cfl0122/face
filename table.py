from database import db
from sqlalchemy.dialects.mysql import MEDIUMTEXT


class User(db.Model):
    __tablename__ = 'user'
    personid = db.Column(db.String(50), primary_key=True)
    sceneid = db.Column(db.String(50))
    projectid = db.Column(db.String(50))
    tenantid = db.Column(db.String(200))
    filename = db.Column(db.String(50))
    x1 = db.Column(db.Integer)
    y1 = db.Column(db.Integer)
    x2 = db.Column(db.Integer)
    y2 = db.Column(db.Integer)
    feature = db.Column(db.BLOB)


    def __repr__(self):
        return '<User %r>' % self.personId


class UserPicture(db.Model):
    __tablename__='user_picture'
    id = db.Column(db.Integer, primary_key=True)
    personid = db.Column(db.String(50), db.ForeignKey('user.personid'))
    picData = db.Column(MEDIUMTEXT)
    user = db.relationship('User', backref='userPicture', uselist=False)

    def __repr__(self):
        return '<UserPicture %r>' % self.personId




class User2(db.Model):
    __tablename__ = 'user2'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    personid = db.Column(db.String(50))
    projectid = db.Column(db.String(50))
    tenantid = db.Column(db.String(50))
    sceneid = db.Column(db.String(50))
    imageid = db.Column(db.String(50))
    pictype = db.Column(db.String(50))
    filename = db.Column(db.String(50))
    create_time = db.Column(db.TIMESTAMP)
    x1 = db.Column(db.Integer)
    y1 = db.Column(db.Integer)
    x2 = db.Column(db.Integer)
    y2 = db.Column(db.Integer)
    feature = db.Column(db.BLOB)
    userPicture = db.relationship('UserPicture2', backref='user', uselist=False)

    def __repr__(self):
        return '<User %r>' % self.personId


class UserPicture2(db.Model):
    __tablename__ = 'user_picture2'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user2.id'))
    pic_data = db.Column(MEDIUMTEXT)


    def __repr__(self):
        return '<UserPicture2 %r>' % self.id


class UserProject(db.Model):
    __tablename__ = 'user_project'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    personid = db.Column(db.String(50))
    perjectid = db.Column(db.String(50))