# -*- coding: utf-8 -*-
# author:BerryHN
# max pooling是CNN当中的最大值池化操作，其实用法和卷积很类似
# 有些地方可以从卷积去参考【TensorFlow】tf.nn.conv2d是怎样实现卷积的？
# tf.nn.max_pool(value, ksize, strides, padding, name=None)
# 参数是四个，和卷积很类似：
# 第一个参数value：需要池化的输入，一般池化层接在卷积层后面，所以输入通常是feature map，依然是[batch, height, width, channels]这样的shape
# 第二个参数ksize：池化窗口的大小，取一个四维向量，一般是[1, height, width, 1]，因为我们不想在batch和channels上做池化，所以这两个维度设为了1
# 第三个参数strides：和卷积类似，窗口在每一个维度上滑动的步长，一般也是[1, stride,stride, 1]
# 第四个参数padding：和卷积类似，可以取'VALID' 或者'SAME'
# 返回一个Tensor，类型不变，shape仍然是[batch, height, width, channels]这种形式

import tensorflow as tf

a = tf.constant([
    [[1.0, 2.0, 3.0, 4.0],
     [5.0, 6.0, 7.0, 8.0],
     [8.0, 7.0, 6.0, 5.0],
     [4.0, 3.0, 2.0, 1.0]],
    [[4.0, 3.0, 2.0, 1.0],
     [8.0, 7.0, 6.0, 5.0],
     [1.0, 2.0, 3.0, 4.0],
     [5.0, 6.0, 7.0, 8.0]]
])

a = tf.reshape(a, [1, 4, 4, 2])

pooling = tf.nn.max_pool(a, [1, 2, 2, 1], [1, 1, 1, 1], padding='VALID')
with tf.Session() as sess:
    print("image:")
    image = sess.run(a)
    print (image)
    print("reslut:")
    result = sess.run(pooling)
    print (result)
    print result.shape