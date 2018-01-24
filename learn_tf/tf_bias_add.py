# -*- coding: utf-8 -*-
# author:BerryHN
import tensorflow  as tf
# tf.nn.bias_add(value, bias, name=None)
# 解释，这个函数的作用是将偏差项bias加到value上面
# 这个操作你可以看做tf.add的一个特例，其中bias必须是一纬的，该api支持广播形式，因此value可以有任何纬度，但是该pai不想tf.add  可以让bias的纬度和value的最后一纬不同

# 输入参数：
# value：一个tensor 数据类型必须是float，double ，int64，int32，uint8，int16，int8或者
# complex64
# bias：一个一位的tensor，数据纬度和value的最后一维相同，数据类型必须和value相同
# name  为这个操作的一个名字

# 输出参数：
# 一个tensor  数据类型和value相同

a=tf.constant([[1,1],[2,2],[3,3]],dtype=tf.float32)
b=tf.constant([1,-1],dtype=tf.float32)
c=tf.constant([1],dtype=tf.float32)

with tf.Session() as sess:
    print('bias_add:')
    print(sess.run(tf.nn.bias_add(a, b)))
    #执行下面语句错误
    #print(sess.run(tf.nn.bias_add(a, c)))

    print('add:')
    print(sess.run(tf.add(a, c)))