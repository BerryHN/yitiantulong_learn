# -*- coding: utf-8 -*-
# author:BerryHN
import tensorflow as tf
import numpy  as np
c1 = []

a1 = np.array([2,3,4,5])

b1 = a1.reshape([1,1,1,4])



a2 = np.array([11,12,13,14])

b2 = a2.reshape([1,1,1,4])
print b2
a3 = np.array([21,22,23,24])

b3 = a3.reshape([1,1,1,4])
print b3

c1.append(b1)
print c1
c1.append(b2)
print c1
c1.append(b3)
print c1
d = tf.concat(c1,3)
print d
num = 3*4
f = tf.reshape(d,[-1,12])
print f

h = tf.nn.dropout(f, 0.2)




with tf.Session() as sess:
    print sess.run(d)
    print d
    print f
    print h.eval()


