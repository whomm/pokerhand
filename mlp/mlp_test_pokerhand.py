#!/usr/bin/python
# -*- coding: UTF-8 -*-
from sklearn.externals import joblib
from mlp_pokerhand import load_data, foo
'''
利用测试数据测试之前的模型
输入：../data/random-testing.data ./good.modle
输出：验证正确和错误的数目
'''

if __name__=="__main__":
    mlp = joblib.load('./good.modle')

    prex,prey = load_data("../data/random-testing.data")

    rr = mlp.predict(prex)



    rightcount = 0
    errorcount = 0

    result = prey-rr
    lineno = 1
    for i in result:
        noterror = 1
        for j in i:
            if int(j) != 0:
                errorcount += 1
                noterror = 0

                print("errorline:",lineno)
                print("predict:",rr[lineno-1])
                print("tetruth:",prey[lineno-1])
                break
        rightcount += noterror
        lineno += 1

    print("rightcount:",rightcount)
    print("errorcount:",errorcount)

