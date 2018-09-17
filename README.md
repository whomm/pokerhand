# pokerhand

uci dataset pokerhand study。

poker hand数据分类学习 （https://archive.ics.uci.edu/ml/datasets/Poker+Hand）

## 目录结构
1. data目录存放 https://archive.ics.uci.edu/ml/machine-learning-databases/poker/ 下的文件
    1. random-testing.data 是从poker-hand-training-true.data 随机抽取的1000行
2. mlp 多层感知神经网络学习和测试模型（sklearn）
    1.  hidden_layer_sizes=(260,156,52), ='tanh', solver='lbfgs',  正确率 98.92%，这个是对于测试集合的一个随机的样本，但是对于特定分类的准确率没有意义。
    2. 特定分类的准确率会很低 ， 9 分类的数据就几条训练不出好的模型。
3. svm 支持向量机的方法（https://www.csie.ntu.edu.tw/~cjlin/libsvm/）
    1. 数据来源： https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/multiclass.html#poker
    2. 处理方法 awk -f datapre.awk poker > poker.t


