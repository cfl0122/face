import face_model
import argparse
import cv2
import json
import sys
import numpy as np

parser = argparse.ArgumentParser(description='face model test')
# general
parser.add_argument('--image-size', default='112,112', help='')
parser.add_argument('--model', default='E:\insightface-master\models\model,00', help='path to load model.')
parser.add_argument('--ga-model', default='', help='path to load model.')
parser.add_argument('--gpu', default=0, type=int, help='gpu id')
parser.add_argument('--det', default=0, type=int, help='mtcnn option, 1 means using R+O, 0 means detect from begining')
parser.add_argument('--flip', default=0, type=int, help='whether do lr flip aug')
parser.add_argument('--threshold', default=1.24, type=float, help='ver dist threshold')
args = parser.parse_args()

model = face_model.FaceModel(args)
img = cv2.imread('C:\\Users\\DELL\\Pictures\\1.jpg')
# img = cv2.imread('22.jpg')
img = model.get_input(img)
#print(img.shape)
f1 = model.get_feature(img)

print(json.dumps(f1))
#print(f1[0:10])
# gender, age = model.get_ga(img)
# print(gender)
# print(age)
#sys.exit(0)
img = cv2.imread('Tom_Hanks_54745.png')
img = cv2.imread('C:\\Users\\DELL\\Pictures\\2.jpg')
img = model.get_input(img)
f2 = model.get_feature(img)
dist = np.sum(np.square(f1-f2))
print(dist)
sim = np.dot(f1, f2.T)
print(sim)
#diff = np.subtract(source_feature, target_feature)
#dist = np.sum(np.square(diff),1)

img = cv2.imread('C:\\Users\\DELL\\Pictures\\3.jpg')
img = model.get_input(img)
f3 = model.get_feature(img)
dist = np.sum(np.square(f1-f3))
print(dist)
sim = np.dot(f1, f3.T)
print(sim)




img = cv2.imread('C:\\Users\\DELL\\Pictures\\4.jpg')
img = model.get_input(img)
f4 = model.get_feature(img)
dist = np.sum(np.square(f1-f4))
print(dist)
sim = np.dot(f1, f4.T)
print(sim)



img = cv2.imread('C:\\Users\\DELL\\Pictures\\5.jpg')
img = model.get_input(img)
f5 = model.get_feature(img)

dist = np.sum(np.square(f1-f5))
print(dist)
sim = np.dot(f1, f5.T)
print(sim)


img = cv2.imread('C:\\Users\\DELL\\Pictures\\6.jpg')
img = model.get_input(img)
f6 = model.get_feature(img)
dist = np.sum(np.square(f1-f6))
print(dist)
sim = np.dot(f1, f6.T)
print(sim)

img = cv2.imread('C:\\Users\\DELL\\Pictures\\7.jpg')
img = model.get_input(img)
f7 = model.get_feature(img)
dist = np.sum(np.square(f1-f7))
print(dist)
sim = np.dot(f1, f7.T)
print(sim)


img = cv2.imread('C:\\Users\\DELL\\Pictures\\8.jpg')
img = model.get_input(img)
f8 = model.get_feature(img)
dist = np.sum(np.square(f1-f7))
print(dist)
sim = np.dot(f3, f7.T)
print(sim)


img = cv2.imread('C:\\Users\\DELL\\Pictures\\9.jpg')
img = model.get_input(img)
f9 = model.get_feature(img)
dist = np.sum(np.square(f3-f7))
print(dist)
sim = np.dot(f3, f7.T)
print(sim)


dist = np.sum(np.square(f6-f7))
print(dist)
sim = np.dot(f6, f7.T)
print(sim)



dist = np.sum(np.square(f1-f7))
print(dist)
sim = np.dot(f1, f7.T)
print(sim)


dist = np.sum(np.square(f1-f6))
print(dist)
sim = np.dot(f1, f6.T)
print(sim)