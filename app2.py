# -*- coding: utf-8 -*-
from flask import Flask
from database import db
from tencent_bp import tencent
# from platform_bp import platform
from platform_bp2 import platform2
app = Flask(__name__,template_folder="template")
app.register_blueprint(tencent)
# app.register_blueprint(platform)
app.register_blueprint(platform2)


# app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///e:/user/user.db'
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://chenfeilong:fka!asdaWFT523@10.8.108.12/chenfeilong'
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "12345678"
app.config["WTF_CSRF_ENABLED"]=False
db.init_app(app)

# db.drop_all()
# db.create_all()


if __name__ == '__main__':
    app.run(debug=True,)



