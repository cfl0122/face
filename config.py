from deploy import face_model_V2_retina
import argparse,os




uploaddir ='./upload/'
resultdir='./result/'
tempdir='./temp/'
threshold=0.54
publickey_filepath = "rsa_public.pem"
sslfile         ='./server/'


os.environ["MXNET_CUDNN_AUTOTUNE_DEFAULT"] = '0'
parser = argparse.ArgumentParser(description='face model test')
# general
parser.add_argument('--image-size', default='112,112', help='')
parser.add_argument('--model', default='models/model,00', help='path to load model.')
parser.add_argument('--ga-model', default='', help='path to load model.')
parser.add_argument('--gpu', default=0, type=int, help='gpu id')
parser.add_argument('--det', default=0, type=int, help='mtcnn option, 1 means using R+O, 0 means detect from begining')
parser.add_argument('--flip', default=0, type=int, help='whether do lr flip aug')
parser.add_argument('--threshold', default=1.24, type=float, help='ver dist threshold')
args = parser.parse_args()

model = face_model_V2_retina.FaceModel(args)


