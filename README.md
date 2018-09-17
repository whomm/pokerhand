# pokerhand

uci dataset pokerhand study。

poker hand数据分类学习 （https://archive.ics.uci.edu/ml/datasets/Poker+Hand）


1. data目录存放 https://archive.ics.uci.edu/ml/machine-learning-databases/poker/ 下的文件
    1. random-testing.data 是从poker-hand-training-true.data 随机抽取的1000行
2. mlp 多层感知神经网络学习和测试模型（sklearn）
    1.  hidden_layer_sizes=(260,156,52), ='tanh', solver='lbfgs',  正确率 98.92%，这个是对于测试集合的一个随机的样本，但是对于特定分类的准确率没有意义。
    2. 特定分类的准确率会很低 ， 9 分类的数据就几条训练不出好的模型。
3. svm 支持向量机的方法（https://www.csie.ntu.edu.tw/~cjlin/libsvm/）
    1. 数据来源： https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/multiclass.html#poker
    2. 处理方法 awk -f datapre.awk poker > poker.t
    3. 把花色 和 大小映射到 1 - 52 之间 直接使用 svm -t 2 -c 100
        1. ../libsvm-3.23/svm-train -t 2 -c 100 ./poker.t
        2.  awk -f mpre.awk  poker >mp
        3.  awk -f mpre.awk  poker.t >mp.t
        4. 训练数据准确率Accuracy = 92.527% (23141/25010) (classification)
        5. 随机10000条测试数据 Accuracy = 28.06% (2806/10000) (classification)
4. 其他
    1. poker（德州扑克手牌的分类） https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/multiclass.html
    2. 来源： https://archive.ics.uci.edu/ml/datasets/Poker+Hand
    3. 相关论文：
        1. https://www.seas.upenn.edu/~cse400/CSE400_2006_2007/Pfund/PfundPaper.pdf Support Vector Machines in the Machine Learning Classifier for a Texas Hold’em Poker Bot
        2. http://www.wseas.us/e-library/conferences/crete2002/papers/444-494.pdf    Evolutionary Data Mining With Automatic Rule Generalization
        3. https://pdfs.semanticscholar.org/905a/0f27e520b3f2627863f9fa94a87fda7060cd.pdf NN-based Poker Hand Classification and Game Playing
        4. https://eembdersler.files.wordpress.com/2010/09/2014913024-gokaydisken-project.pdf PREDICTING POKER HAND’S STRENGTH WITH ARTIFICIAL NEURAL NETWORKS


