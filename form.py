from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,FloatField,TimeField
from wtforms.validators import DataRequired

class FaceAddForm(FlaskForm):

    tenantid = StringField("租户ID",validators=[DataRequired()])
    projectid = StringField("项目ID",validators=[])
    personid = StringField("用户ID",validators=[])
    sceneid = StringField("场景ID")
    picture = StringField("图片base64编码",validators=[DataRequired()])
    imageid = StringField("人脸或人体ID",validators=[])
    pictype = StringField("图片类型：face或body",validators=[DataRequired()])


class FaceDeleteForm(FlaskForm):
    tenantid = StringField("租户ID",validators=[DataRequired()])
    projectid = StringField("项目ID",validators=[])
    personid = StringField("用户ID",validators=[DataRequired()])
    sceneid = StringField("场景ID")



class FaceSearchForm(FlaskForm):
    tenantid = StringField("租户ID",validators=[DataRequired()])
    projectid = StringField("项目ID",validators=[])
    picture = StringField("图片base64编码",validators=[DataRequired()])
    sceneid = StringField("场景ID")

class FaceSearchMultiForm(FlaskForm):
    tenantid = StringField("租户ID",validators=[DataRequired()])
    projectid = StringField("项目ID",validators=[])
    picture = StringField("图片base64编码",validators=[DataRequired()])
    sceneid = StringField("场景ID")
    topn = IntegerField("期望返回的结果个数，默认值为10")
    threshold = FloatField("人脸相似度阈值")
    livedetect = IntegerField("是否需要做活体检测")


class TraceRouteForm(FlaskForm):
    tenantid = StringField("租户ID",validators=[DataRequired()])
    projectid = StringField("项目ID",validators=[])
    picture = StringField("图片base64编码",validators=[DataRequired()])
    sceneid = StringField("场景ID")
    starttime = IntegerField("起始时间，时间戳",validators=[DataRequired()])
    endtime = IntegerField("起始时间，时间戳",validators=[DataRequired()])
    pictype = StringField("图片类型：“face”、“body”和“all”",validators=[DataRequired()])
