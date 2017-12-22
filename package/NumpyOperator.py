# -*- coding:utf-8 -*-

# 导入NumPy函数库，一般都是用这样的形式(包括别名np，几乎是约定俗成的)
import numpy as np

if __name__ == "__main__":
    # 标准Python的列表(list)中，元素本质是对象。
    # 如：L = [1, 2, 3]，需要3个指针和三个整数对象，对于数值运算比较浪费内存和CPU。
    # 因此，Numpy提供了ndarray(N-dimensional array object)对象：存储单一数据类型的多维数组。

    print "------------------------List转成ndarray------------------------"
    # # 1.使用array创建
    # 通过array函数传递list对象
    L = [1, 2, 3, 4, 5, 6]
    print "L = ", L
    # 将List转成ndarray
    a = np.array(L)
    print "a = ", a
    print type(a), type(L)

    print "------------------------创建多维数组------------------------"
    # 若传递的是多层嵌套的list，将创建多维数组
    b = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    print b

    print "------------------------获得数组大小------------------------"
    # 数组大小可以通过其shape属性获得
    print a.shape
    print b.shape

    print "------------------------修改数组大小------------------------"
    # 数组的转置 返回一个新的数组 不会改变原有数组的值
    transpose = b.transpose()
    print transpose
    # 也可以强制修改shape
    # 注：从(3,4)改为(4,3)并不是对数组进行转置，而只是改变每个轴的大小，数组元素在内存中的位置并没有改变
    b.shape = 4, 3
    print b
    # 当某个轴为-1时，将根据数组元素的个数自动计算此轴的长度
    b.shape = 2, -1
    print b
    print b.shape

    b.shape = 3, 4
    print b
    # 使用reshape方法，可以创建改变了尺寸的新数组，原数组的shape保持不变
    c = b.reshape((4, -1))
    print "b = \n", b
    print 'c = \n', c

    print "------------------------数组b和c共享内存------------------------"
    # 数组b和c共享内存，修改任意一个将影响另外一个
    b[0][1] = 20
    print "b = \n", b
    print "c = \n", c

    print "------------------------获取数组元素类型------------------------"
    # 数组的元素类型可以通过dtype属性获得
    print a.dtype
    print b.dtype

    print "------------------------指定数组元素类型------------------------"
    # 可以通过dtype参数在创建时指定元素类型
    d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], dtype=np.float)
    print d

    print "------------------------改变数组元素类型------------------------"
    # 如果更改元素类型，可以使用astype安全的转换
    f = d.astype(np.int)
    print f


    # 如果生成一定规则的数据，可以使用NumPy提供的专门函数
    # arange函数类似于python的range函数：指定起始值、终止值和步长来创建数组
    print "------------------------np.arange按照步长创建等差数组------------------------"
    a = np.arange(1, 10, 0.5)
    print a

    print "------------------------np.linspace按照个数创建等差数组------------------------"
    # linspace函数通过指定起始值、终止值和元素个数来创建数组，缺省包括终止值
    # 可以通过endpoint关键字指定是否包括终值
    b = np.linspace(1, 100, 10, endpoint=False)
    print 'b = ', b

    print "------------------------np.logspace按照个数创建等比数组------------------------"
    # 和linspace类似，logspace可以创建等比数列
    # 起始指数 终止指数 个数 是否包含终止值 底数
    d = np.logspace(1, 4, 2, endpoint=True, base=2)
    print d

    print "------------------------np.fromstring按照字节序列创建数组------------------------"
    # 使用 frombuffer, fromstring, fromfile等函数可以从字节序列创建数组
    s = 'abcdzzzz'
    g = np.fromstring(s, dtype=np.int8)
    print g

    # 根据整数数组存取：当使用整数序列对数组元素进行存取时，
    # 将使用整数序列中的每个元素作为下标，整数序列可以是列表(list)或者数组(ndarray)。
    print "------------------------使用整数序列作为下标获得数组------------------------"
    # 使用整数序列作为下标获得的数组不和原始数组共享数据空间。
    a = np.logspace(0, 9, 10, base=2)
    print a
    i = np.arange(0, 10, 2)
    print i
    # 利用i取a中的元素
    b = a[i]
    print b
    # b的元素更改，a中元素不受影响
    b[2] = 1.6
    print b
    print a

    print "------------------------使用整数序列作为下标获得数组------------------------"
    # 使用布尔数组i作为下标存取数组a中的元素：返回数组a中所有在数组b中对应下标为True的元素
    # 生成10个满足[0,1)中均匀分布的随机数
    a = np.random.rand(10)
    print a
    # 大于0.5的元素索引
    print a > 0.5
    # 大于0.5的元素
    b = a[a > 0.5]
    print b
    # 将原数组中大于0.5的元素截取成0.5
    a[a > 0.5] = 0.5
    print a
    # b不受影响
    print b

    print "------------------------行+列------------------------"
    a = np.arange(0, 60, 10)    # 行向量
    print 'a = ', a
    b = a.reshape((-1, 1))      # 转换成列向量
    print b
    c = np.arange(6)
    print c
    f = b + c   # 行 + 列
    print f
    # 合并上述代码：
    a = np.arange(0, 60, 10).reshape((-1, 1)) + np.arange(6)
    print a
    print "------------------------二维数组的切片------------------------"
    # # # 二维数组的切片
    print a[[0, 1, 2], [2, 3, 4]]
    print a[4, [2, 3, 4]]
    print a[4:, [2, 3, 4]]
    i = np.array([True, False, True, False, False, True])
    print a[i]
    print a[i, 3]
