# -*- coding: utf-8 -*-
# author:BerryHN
import jieba
import codecs
import re
from zhon.hanzi import punctuation
import os
base_path = os.path.abspath(os.path.dirname(__file__))
file_name = os.path.join(base_path,'../data/ab_utf_8.txt')
file_name2 = os.path.join(base_path,'../data/ab_utf_8_segmented.txt')
fin = codecs.open(file_name,'r', encoding='utf-8')
fou = codecs.open(file_name2, 'w', encoding='utf-8')

line = fin.readline()

while line:
    newline = jieba.cut(line, cut_all=False)
    str_out = ' '.join(newline)
    #str_out = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？?、~@#￥%……&*（）]+".decode("utf8"), " ".decode("utf8"), str_out)
    #str_out = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+".decode("utf8"), " ".decode("utf8"), str_out)
    str_out = re.sub(ur"[%s]+" % punctuation, " ", str_out)
    fou.write(str_out+'\n')
    line = fin.readline()
fin.close()
fou.close()


