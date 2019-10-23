import mxnet as mx
from mxnet import ndarray as nd
try:
    ctx=mx.gpu()
    aa=nd.zeros((1,),ctx=ctx)
except:
    ctx=mx.cpu()
print(ctx)