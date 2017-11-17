# -*- coding:utf-8 -*-

"""
http://yann.lecun.com/exdb/mnist/
t10k-images-idx3-ubyte	t10k-labels-idx1-ubyte	train-images-idx3-ubyte	train-labels-idx1-ubyte
http://blog.csdn.net/ni_guang2010/article/details/53069579
http://blog.csdn.net/zugexiaodui/article/details/77130862

"""
import struct

import matplotlib.pyplot as plt
import numpy as np
# Import datasets, classifiers and performance metrics
from sklearn import svm


def loadImageSet(filename):
    print "load image set",filename
    binfile= open(filename, 'rb')
    buffers = binfile.read()

    head = struct.unpack_from('>IIII' , buffers ,0)
    print "head,",head

    offset = struct.calcsize('>IIII')
    imgNum = head[1]
    width = head[2]
    height = head[3]
    #[60000]*28*28
    bits = imgNum * width * height
    bitsString = '>' + str(bits) + 'B' #like '>47040000B'
    print bitsString
    imgs = struct.unpack_from(bitsString,buffers,offset)

    binfile.close()
    imgs = np.reshape(imgs,[imgNum,1,width*height])
    print "load imgs finished"
    return imgs

def loadLabelSet(filename):

    print "load label set",filename
    binfile = open(filename, 'rb')
    buffers = binfile.read()

    head = struct.unpack_from('>II' , buffers ,0)
    print "head,",head
    imgNum=head[1]

    offset = struct.calcsize('>II')
    numString = '>'+str(imgNum)+"B"
    labels = struct.unpack_from(numString , buffers , offset)
    binfile.close()
    labels = np.reshape(labels,[imgNum,1])

    print 'load label finished'
    return labels

def testRead(filename,imindex):
    binfile = open(filename , 'rb')
    buf = binfile.read()

    index = 0
    magic, numImages , numRows , numColumns = struct.unpack_from('>IIII' , buf , index)
    print "magic:",magic
    print "numRows:",numRows
    print "numColumns:",numColumns

    index += struct.calcsize('>IIII')
    index += imindex * numRows * numColumns

    bits = numRows*numColumns
    bitsString = '>' + str(bits) + 'B'

    im = struct.unpack_from(bitsString ,buf, index)


    im = np.array(im)
    im = im.reshape(numRows,numColumns)

    fig = plt.figure()
    plotwindow = fig.add_subplot(111)
    plt.imshow(im , cmap='gray')
    plt.show()

def showImage(imgs,labels,index):
    print labels[index][0]
    im = imgs[index].reshape(28,28)
    fig = plt.figure()
    plotwindow = fig.add_subplot(111)
    plt.imshow(im , cmap='gray')
    plt.show()

# create model
# SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
#     decision_function_shape='ovr', degree=3, gamma='auto', kernel='rbf',
#     max_iter=-1, probability=False, random_state=None, shrinking=True,
#     tol=0.001, verbose=False)
def create_svm(dataMat, dataLabel, decision='ovr'):
    clf = svm.SVC(decision_function_shape=decision)
    clf.fit(dataMat, dataLabel)
    return clf

if __name__ == '__main__':
    imagefile = '/Users/liuche/project/github/digits/train-images-idx3-ubyte'
    labelfile = '/Users/liuche/project/github/digits/train-labels-idx1-ubyte'
    imgs = loadImageSet(imagefile)
    labels = loadLabelSet(labelfile)
    # showImage(imgs,labels,10)
    n_samples = len(imgs)
    data = imgs.reshape((n_samples, -1))
    clf = create_svm(data,labels)
    testimagefile = '/Users/liuche/project/github/digits/t10k-images-idx3-ubyte'
    testlabelfile = '/Users/liuche/project/github/digits/t10k-labels-idx1-ubyte'
    testimgs = loadImageSet(testimagefile)
    testlabels = loadLabelSet(testlabelfile)


    print("test dataMat shape: {0}, test dataLabel len: {1} ".format(testimagefile.shape, len(testlabelfile)))

    #print("test dataLabel: {}".format(len(tdataLabel)))
    n_samples = len(testimgs)
    data = testimgs.reshape((n_samples, -1))
    preResult = clf.predict(testimgs[0])
    print preResult


    # testRead(imagefile,2)
    # testRead(imagefile,3)
