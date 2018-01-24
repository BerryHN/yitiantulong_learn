# -*- coding: utf-8 -*-
# author:BerryHN
import tensorflow  as tf
# 用tensorflow做CNN_TEXT文本分类时，看到这个API，然后去官网查了一下，再看了一下别的资料，算是明白它的处理方式了。
# 　　首先，明确一点，tf.argmax可以认为就是np.argmax。tensorflow使用numpy实现的这个API。
# 　　
# 　　简单的说，tf.argmax就是返回最大的那个数值所在的下标。
# 　　
# 　　这个很好理解，只是tf.argmax()的参数让人有些迷惑，比如，tf.argmax(array, 1)和tf.argmax(array, 0)有啥区别呢？
# 　　
# 　　这里面就涉及到一个概念：axis。上面例子中的1和0就是axis。我先笼统的解释这个问题，设置axis的主要原因是方便我们进行多个维度的计算。
#
# 　　在实例面前，再多的语言都是苍白的呀，上例子！
#
# axis = 0:
# 　　你就这么想，0是最大的范围，所有的数组都要进行比较，只是比较的是这些数组相同位置上的数
#
# axis = 1:
# 　　等于1的时候，比较范围缩小了，只会比较每个数组内的数的大小，结果也会根据有几个数组，产生几个结果。





import numpy as np
test = np.array([[1, 2, 3], [2, 3, 4], [5, 4, 3], [8, 7, 2]])
t1 = np.argmax(test, 0)
t2 = np.argmax(test, 1)

print t1
print t2


