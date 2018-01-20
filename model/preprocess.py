# -*- coding: utf-8 -*-
# author:BerryHN
import codecs
import os
base_path = os.path.abspath(os.path.dirname(__file__))
file_name = os.path.join(base_path,'../data/ab.txt')
file_name2 = os.path.join(base_path,'../data/ab_utf_8.txt')
fin = codecs.open(file_name,'r',encoding='GB18030')
fou = codecs.open(file_name2,'w',encoding='utf-8')
line = fin.readline()
while line:
    newline = line
    fou.write(newline+'\n')
    line = fin.readline()
fin.close()
fou.close()