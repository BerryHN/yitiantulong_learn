# -*- coding: utf-8 -*-
# author:BerryHN
import tensorflow  as tf
num_filters = 128
b = tf.Variable(tf.constant(0.1, shape=[num_filters]), name="b")
print b



filter_size = 3
embedding_size= 128

filter_shape = [filter_size, embedding_size, 1, num_filters]
W = tf.Variable(tf.truncated_normal(filter_shape, stddev=0.1), name="W")
print W






# with tf.Session()  as sess:
#     sess.run(b)
#     print b