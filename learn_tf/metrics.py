# -*- coding: utf-8 -*-
# author:BerryHN
from sklearn import metrics
from sklearn.metrics import accuracy_score,classification_report
import numpy  as np
a = [1,2,2,3,3,3,4,4,4,4,1]
b = [1,2,1,2,3,3,3,4,4,4,1]

print  '-------混淆矩阵-------'
c = metrics.confusion_matrix(a,b)

print c

print '------模型分类正确率------'

d = accuracy_score(a,b)
d = round(d*100,2)
format = '%.2f%s'%(round(d,2),'%')
print format

print '---------分类模型精确率和召回率--------'
print metrics.classification_report(a, b, target_names=['0','1','2','3'])










