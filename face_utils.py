import cv2
import numpy as np
import os

# 输入一张包含人脸的图片，返回一个人脸特征向量和一个矩形框
def gen_feature(picture, model):
    img = cv2.imdecode(np.fromfile(picture,dtype=np.uint8),cv2.IMREAD_COLOR)
    r = model.get_input(img)
    if r is not None:
        img,bbox=r
        f = model.get_feature(img)
        return f,bbox
    else:
        return None


# 输入一张包含人脸的图片，返回多个人脸特征向量和多个矩形框
def gen_feature_multi(picture, model):
    img = cv2.imdecode(np.fromfile(picture,dtype=np.uint8),cv2.IMREAD_COLOR)
    r = model.get_input_multi(img)
    if r is not None:
        fs=[]
        face_imgs,bboxs=r
        for i in range(len(face_imgs)):
            f = model.get_feature(face_imgs[i])
            fs.append(f)
    else:
        return None
    return fs,bboxs

# 输入类型如[(6,212),(5,322),(7:14)...]返回value中元素最大的那个tuple 如（5，322）
def get_max_value_idx(a):
    b=np.array(a).T
    c=b.argmax(axis=1)[1]
    d = a[c]
    return d


# 输入一张包含人脸的图片、人脸特征向量和矩形框，绘制的结果图片保存到结果目录
def plotpic(input_img,output_dir, feats_rects):

    img = cv2.imdecode(np.fromfile(input_img,dtype=np.uint8),cv2.IMREAD_COLOR)

    sim,ret = feats_rects
    for i in range(len(sim)):
        ret_=ret[i]
        if len(sim[i]) !=0 :
            sim_=get_max_value_idx(sim[i])
            cv2.putText(img,str(sim_),(ret_[0]-20,ret_[1]-12),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

        cv2.rectangle(img, (ret_[0], ret_[1]), (ret_[2], ret_[3]), (0, 255, 0), 2)
    f=os.path.join(output_dir,os.path.split(input_img)[-1])
    cv2.imencode('.jpg', img)[1].tofile(f)



