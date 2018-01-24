# -*- coding: utf-8 -*-
# author:BerryHN
# tf.reshape(tensor, shape, name=None)
# 函数的作用是将tensor变换为参数shape的形式。
# 其中shape为一个列表形式，特殊的一点是列表中可以存在-1。-1代表的含义是不用我们自己指定这一维的大小，函数会自动计算，但列表中只能存在一个-1。（当然如果存在多个-1，就是一个存在多解的方程了）
#
# 好了我想说的重点还有一个就是根据shape如何变换矩阵。其实简单的想就是，
#
# reshape（t, shape） => reshape(t, [-1]) => reshape(t, shape)
#
# 首先将矩阵t变为一维矩阵，然后再对矩阵的形式更改就可以了。
import tensorflow  as tf
t = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print tf.reshape(t,[3,3])

f = tf.reshape(t,[-1,9])
with tf.Session()  as sess:
    sess.run(f)
    print f.eval()