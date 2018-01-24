# -*- coding: utf-8 -*-
# author:BerryHN
import tensorflow  as tf
import numpy  as np

A = [[1,3,4,5,6]]
B = [[1,3,4,3,2]]
sess = tf.Session()
d= sess.run(tf.equal(A,B))

f = tf.cast(d, 'float')
accuracy = tf.reduce_mean(f)

print sess.run(accuracy)



