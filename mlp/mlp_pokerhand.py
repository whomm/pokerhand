#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
训练数据数据集合并测试少量数据
输入：../data/poker-hand-training-true.data
输出：./good.modle
'''
import io
from scipy.io.arff import loadarff
from sklearn.datasets import get_data_home
from sklearn.externals.joblib import Memory
from sklearn.neural_network import MLPClassifier
import numpy





def foo(var):
    return {
            '9.0': numpy.array([[1.,0,0,0,0,0,0,0,0,0]]),
            '8.0': numpy.array([[0.,1,0,0,0,0,0,0,0,0]]),
            '7.0': numpy.array([[0.,0,1,0,0,0,0,0,0,0]]),
            '6.0': numpy.array([[0.,0,0,1,0,0,0,0,0,0]]),
            '5.0': numpy.array([[0.,0,0,0,1,0,0,0,0,0]]),
            '4.0': numpy.array([[0.,0,0,0,0,1,0,0,0,0]]),
            '3.0': numpy.array([[0.,0,0,0,0,0,1,0,0,0]]),
            '2.0': numpy.array([[0.,0,0,0,0,0,0,1,0,0]]),
            '1.0': numpy.array([[0.,0,0,0,0,0,0,0,1,0]]),
            '0.0': numpy.array([[0.,0,0,0,0,0,0,0,0,0]]),
    }[var]



memory = Memory(get_data_home())

@memory.cache()
def load_data(file):
    train = numpy.loadtxt(open(file, "rb"), delimiter=",", skiprows=0)

    #y变成10列
    y = numpy.zeros((1,10))
    tmpy = train[:,10]
    for element in tmpy.flat:
        y = numpy.append(y,foo(str(element)),axis = 0)
        pass

    #x变成52列

    #把（花色-1）*12+ 当前值  映射到  1-52之间的数字
    tmpx = train[:,0:10]
    tmpx[:,1] = (tmpx[:,0]-1)*13 + tmpx[:,1]
    tmpx[:,3] = (tmpx[:,2]-1)*13 + tmpx[:,3]
    tmpx[:,5] = (tmpx[:,4]-1)*13 + tmpx[:,5]
    tmpx[:,7] = (tmpx[:,6]-1)*13 + tmpx[:,7]
    tmpx[:,9] = (tmpx[:,8]-1)*13 + tmpx[:,9]
    #删除花色
    tmpx = numpy.delete(tmpx, [0,2,4,6,8], axis=1)

    #52的数组标记具体哪一位存在
    ret52 = numpy.zeros((1,52))
    for r in tmpx:
        z52 = numpy.zeros((1,52))
        for i in r:
            z52[0][int(i)-1] = 1
            pass

        ret52 = numpy.append(ret52,z52,axis = 0)
    return ret52[1:], y[1:]



if __name__=="__main__":

    print("load train data")
    x,y = load_data("../data/poker-hand-training-true.data")
    print("load train data ok")

    #http://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html
    mlp = MLPClassifier(hidden_layer_sizes=(208,156,52),
                        activation='tanh',
                        solver='lbfgs',
                        max_iter=10000,
                        shuffle=True,
                        alpha=1e-4,
                        verbose=10,
                        tol=1e-4,
                        random_state=1,
                        learning_rate_init=.1)
    mlp.fit(x, y)
    print("Training set score: %f" % mlp.score(x, y))


    #保存模型到文件
    from sklearn.externals import joblib
    joblib.dump(mlp, 'good.modle')

    #找个小的测试集合测试一下模型
    prex,prey = load_data("../data/random-testing.data")

    print("test x")
    print(prex)
    rr = mlp.predict(prex)
    print("test y")
    print(prey)
    print("predict y")
    print(rr)