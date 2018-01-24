# -*- coding: utf-8 -*-
# author:BerryHN
# 1、tf.truncated_normal使用方法
# tf.truncated_normal(shape, mean=0.0, stddev=1.0, dtype=tf.float32, seed=None, name=None)
#
# 从截断的正态分布中输出随机值。
# 生成的值服从具有指定平均值和标准偏差的正态分布，如果生成的值大于平均值2个标准偏差的值则丢弃重新选择。
#
# 在正态分布的曲线中，横轴区间（μ-σ，μ+σ）内的面积为68.268949%。
# 横轴区间（μ-2σ，μ+2σ）内的面积为95.449974%。
# 横轴区间（μ-3σ，μ+3σ）内的面积为99.730020%。
# X落在（μ-3σ，μ+3σ）以外的概率小于千分之三，在实际问题中常认为相应的事件是不会发生的，基本上可以把区间（μ-3σ，μ+3σ）看作是随机变量X实际可能的取值区间，这称之为正态分布的“3σ”原则。
# 在tf.truncated_normal中如果x的取值在区间（μ-2σ，μ+2σ）之外则重新进行选择。这样保证了生成的值都在均值附近。
#
# 参数:
#
#     shape: 一维的张量，也是输出的张量。
#     mean: 正态分布的均值。
#     stddev: 正态分布的标准差。
#     dtype: 输出的类型。
#     seed: 一个整数，当设置之后，每次生成的随机数都一样。
#     name: 操作的名字
# 2、tf.random_normal使用方法
# tf.random_normal(shape, mean=0.0, stddev=1.0, dtype=tf.float32, seed=None, name=None)
# 从正态分布中输出随机值。
# 参数:
#
#     shape: 一维的张量，也是输出的张量。
#     mean: 正态分布的均值。
#     stddev: 正态分布的标准差。
#     dtype: 输出的类型。
#     seed: 一个整数，当设置之后，每次生成的随机数都一样。
#     name: 操作的名字
import tensorflow as tf
a = tf.Variable(tf.random_normal([2,2],seed=1))
b = tf.Variable(tf.truncated_normal([2,2],seed=2))
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    print(sess.run(a))
    print(sess.run(b))








