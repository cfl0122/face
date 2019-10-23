from flask import Blueprint,request,jsonify
from rsa_utils import rsa_MD5signverify
from form import FaceDeleteForm,FaceSearchForm,FaceAddForm,FaceSearchMultiForm,TraceRouteForm
from table import UserPicture2,User2
import base64,time,logging,datetime
import pickle as pk
from config import uploaddir,tempdir,threshold,publickey_filepath,model,resultdir
from database import db
from face_utils import *
from mysnow import MySnow


LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='logger.log', level=logging.INFO,format=LOG_FORMAT)
snow = MySnow(dataID="00")


tencent = Blueprint('tencent',__name__)


@tencent.before_app_first_request
def init():
    if not os.path.exists(tempdir):
        os.makedirs(tempdir)
    if not os.path.exists(uploaddir):
        os.makedirs(uploaddir)
    if not os.path.exists(resultdir):
        os.makedirs(resultdir)


@tencent.before_request
def auth():
    # return None
    Timestamp = request.headers.get("Timestamp")
    Nonce =  request.headers.get("Nonce")
    Auth = request.headers.get("Auth")
    message = Timestamp + '&' + Nonce
    try:
        signature = rsa_MD5signverify(message=message, signature=Auth, publickey_filepath=publickey_filepath)
        if not signature:
            resp = {"code": 410, "message": "用户验证失败"}
            return jsonify(resp)
    except Exception as e:
        e.with_traceback()
        resp = {"code": 410, "message": "用户验证失败"}
        return jsonify(resp)


@tencent.route('/v1/faceorbody/newperson',methods=['POST'])
def tencent_api_add():
    try:

        form = FaceAddForm()
        if form.validate_on_submit():

            id = snow.get_id()
            tenantid = form.tenantid.data
            projectid = form.projectid.raw_data
            if projectid is None or projectid == "":
                projectid=[]
            personid = form.personid.data
            sceneid = form.sceneid.data
            picture = form.picture.data
            imageid = form.imageid.data
            if imageid == "" or imageid is None:
                imageid = id
            pictype = form.pictype.data
            filename = id + '.jpg'
            imgdata = base64.b64decode(picture)
            file = open(uploaddir + filename, 'wb')
            file.write(imgdata)
            file.close()

            r = gen_feature(uploaddir + filename,model)
            if r is not None:
                f, bbox = r
                x1, y1, x2, y2 = bbox
                if projectid is  None:
                    projectid=[]

                userPicture=UserPicture2(pic_data=picture)
                user=User2(personid=personid,
                           projectid=" ".join(projectid),
                          filename=filename,
                          feature=pk.dumps(f),
                          x1=x1,
                          y1=y1,
                          x2=x2,
                          y2=y2,
                          tenantid=tenantid,
                          sceneid=sceneid,
                          pictype=pictype,
                          imageid=imageid,
                           userPicture=userPicture)
                db.session.add(user)
                db.session.commit()

                resp = {"code": 200, "message": "ok", "imageid": imageid, "projectid": projectid}

            else:
                resp = {"code": 1210, "message": "图片不符合要求"}

        else:
            logging.warning(form.errors)
            resp = {"code": 400, "message": "请求参数不完整或不正确"}
        return jsonify(resp)
    except:

        resp = {"code": 500, "message": "内部请求出错"}
        return jsonify(resp)


@tencent.route('/v1/face/deleteperson',methods=['POST'])
def tencent_api_del():
    try:
        form = FaceDeleteForm()
        if form.validate_on_submit():
            tenantid = form.tenantid.data
            projectid = form.projectid.raw_data
            if projectid is None or projectid == "":
                projectid=[]
            personid = form.personid.data
            sceneid = form.sceneid.data



            user = User2.query.filter_by(personid=personid,tenantid=tenantid,sceneid=sceneid).first()
            if user is None:
                resp = {"code": 1404, "message": "删除person个体失败，不存在该个体"}
                return jsonify(resp)


            x=user.projectid.split(" ")
            if x[0]=='':
                x=[]
            x=set(x)
            y=set(projectid)
            z=x.difference(y)
            print(len(z))
            if len(z) == 0:

                userPictures = UserPicture2.query.filter_by(user_id=user.id).delete()
                # [db.session.delete(i) for i in userPictures]
                db.session.delete(user)

            else:
                user.projectid=" ".join(z)
            db.session.commit()

            resp = {"code": 200, "message": "ok", "projectid": projectid}
        else:
            logging.warning(form.errors)
            resp = {"code": 400, "message": "请求参数不完整或不正确"}
        return jsonify(resp)
    except:
        resp = {"code": 500, "message": "内部请求出错"}
        return jsonify(resp)


@tencent.route('/v1/face/identify',methods=['POST'])
def tencent_api_search():
    try:
        form = FaceSearchForm()
        if form.validate_on_submit():
            id = snow.get_id()
            tenantid = form.tenantid.data
            projectid = form.projectid.raw_data
            if projectid is None or projectid == "":
                projectid=[]
            sceneid = form.sceneid.data
            picture = form.picture.data

            filename = id + '.jpg'
            imgdata = base64.b64decode(picture)
            file = open(tempdir + filename, 'wb')
            file.write(imgdata)
            file.close()
            r = gen_feature(tempdir + filename,model)
            if r is not None:
                f1,bbox = r
                data = []
                users = User2.query.filter_by(tenantid=tenantid, sceneid=sceneid).all()
                res_user = None
                res_user_sim = 0.0
                res_projectid = []
                for user in users:
                    f2 = pk.loads(user.feature)
                    dist = np.sum(np.square(f1-f2))
                    sim = np.dot(f1, f2.T)
                    if sim > threshold :
                        if (res_user is  None) or (res_user_sim < sim) :
                            res_user = user
                            res_user_sim = sim
                if res_user is not None:
                    res_projectid = res_user.projectid.split(' ')
                    imageid = res_user.imageid

                if len(res_projectid) == 0 or res_projectid[0] == '':
                    res_projectid = []
                res_projectid = set(res_projectid)
                if len(projectid) != 0:
                    res_projectid = res_projectid.intersection(set(projectid))
                data = []
                for i in res_projectid:


                    result = {"personid": res_user.personid,
                          "projectid": i,
                          "faceid":imageid,
                          "sim": str(res_user_sim) ,
                          "position": [res_user.x1, res_user.y1, res_user.x2-res_user.x1, res_user.y2 - res_user.y1],
                          "livedetect_confidence": None}
                    data.append(result)

                resp = {"code": 200, "message": "ok", "data": data }
            else:
                resp = {"code": 202, "message": "图片不符合要求"}
        else:
            logging.warning(form.errors)
            resp = {"code": 400, "message": "请求参数不完整或不正确"}
        return jsonify(resp)
    except:
        resp = {"code": 500, "message": "内部请求出错"}
        return jsonify(resp)


@tencent.route('/v1/face/identify/multi',methods=['POST'])
def tencent_api_search_multi():
    try:
        form = FaceSearchMultiForm()
        if form.validate_on_submit():
            id = snow.get_id()
            tenantid = form.tenantid.data
            projectid = form.projectid.raw_data
            if projectid is None or projectid == "":
                projectid=[]
            sceneid = form.sceneid.data
            picture = form.picture.data
            topn = form.topn.data
            if topn is None:
                topn = 10
            getthreshold = form.threshold.data
            if getthreshold is not None:
                threshold = getthreshold
            livedetect = form.livedetect.data
            if livedetect is None:
                livedetect = 0


            filename = id + '.jpg'
            imgdata = base64.b64decode(picture)
            file = open(tempdir + filename, 'wb')
            file.write(imgdata)
            file.close()
            r = gen_feature(tempdir + filename,model)
            if r is not None:
                f1,bbox = r
                users = User2.query.filter_by(tenantid=tenantid, sceneid=sceneid).all()
                data = []
                for user in users:
                    print(user.create_time)
                    f2 = pk.loads(user.feature)
                    dist = np.sum(np.square(f1-f2))
                    sim = np.dot(f1, f2.T)
                    if sim > threshold :
                        res_projectid = user.projectid.split(' ')
                        if res_projectid[0] == '':
                            res_projectid = []
                        res_projectid = set(res_projectid)
                        res_projectid = list(res_projectid.intersection(set(projectid)))
                        for i in res_projectid:

                            result={"personid": user.personid,
                                "projectid": i,
                                "faceid": user.imageid,
                                "position": [user.x1,user.y1,user.x2-user.x1,user.y2-user.y1],
                                "sim": str(sim),
                                "livedetect_confidence": '',
                                }
                            data.append(result)

                resp = {"code": 200, "message": "ok", "data": data[0:topn]}
            else:
                resp = {"code": 202, "message": "图片不符合要求"}
        else:
            logging.warning(form.errors)
            resp = {"code": 400, "message": "请求参数不完整或不正确"}
        return jsonify(resp)
    except:
        resp = {"code": 500, "message": "内部请求出错"}
        return jsonify(resp)


@tencent.route('/v1/faceorbody/traceroute',methods=['POST'])
def tencent_api_traceroute():
    # try:
        form = TraceRouteForm()
        if form.validate_on_submit():
            id = snow.get_id()
            tenantid = form.tenantid.data
            projectid = form.projectid.raw_data
            if projectid is None or projectid == "":
                projectid=[]
            sceneid = form.sceneid.data
            picture = form.picture.data

            starttime = form.starttime.data
            starttime=time.localtime(starttime)
            starttime = time.strftime("%Y-%m-%d %H:%M:%S", starttime)
            endtime = form.endtime.data
            endtime=time.localtime(endtime)
            endtime=time.strftime("%Y-%m-%d %H:%M:%S", endtime)
            pictype = form.pictype.data

            filename = id + '.jpg'
            imgdata = base64.b64decode(picture)
            file = open(tempdir + filename, 'wb')
            file.write(imgdata)
            file.close()
            r = gen_feature(tempdir + filename,model)
            if r is not None:

                f1,bbox = r
                sql = User2.query.filter(User2.tenantid==tenantid,

                                                User2.create_time>starttime,

                                                User2.create_time<endtime
                                           ).order_by(User2.create_time)
                if sceneid != "":
                    sql = sql.filter(User2.sceneid==sceneid)
                if pictype != "all":
                    sql = sql.filter(User2.pictype==pictype)
                users = sql.all()

                data = []

                for user in users:
                    f2 = pk.loads(user.feature)
                    dist = np.sum(np.square(f1-f2))
                    sim = np.dot(f1, f2.T)
                    if sim > threshold :
                        res_projectid = user.projectid.split(' ')
                        if res_projectid[0] == '':
                            res_projectid = []
                        res_projectid = set(res_projectid)
                        if len(projectid)!=0:
                            res_projectid = res_projectid.intersection(set(projectid))



                        for i in res_projectid:

                            result={"imageid": user.imageid,
                                "projectid": i,
                                "detecttime": int(datetime.datetime.timestamp(user.create_time)),
                                "sim": str(sim)
                                }
                            data.append(result)

                resp = {"code": 200, "message": "ok", "data": data}
            else:
                resp = {"code": 202, "message": "图片不符合要求"}
        else:
            logging.warning(form.errors)
            resp = {"code": 400, "message": "请求参数不完整或不正确"}
        return jsonify(resp)
    # except:
    #     resp = {"code": 500, "message": "内部请求出错"}
    #     return jsonify(resp)
