# -*- coding: utf-8 -*-
# author:BerryHN
import gensim.models.word2vec  as w2v
import os
import os
base_path = os.path.abspath(os.path.dirname(__file__))
model_file_name = os.path.join(base_path,'../data/ab_model.txt')
w2v_model = w2v.Word2Vec.load(model_file_name)
print '相关度：赵敏->张无忌',w2v_model.similarity('赵敏'.decode('utf-8'),'张无忌'.decode('utf-8'))

print '相关度：周芷若->张无忌',w2v_model.similarity('周芷若'.decode('utf-8'),'张无忌'.decode('utf-8'))

print '相关度：赵敏->谢逊',w2v_model.similarity('赵敏'.decode('utf-8'),'谢逊'.decode('utf-8'))
print "张无忌关系最亲密的10个人"
for k in w2v_model.similar_by_word('张无忌'.decode('utf-8')):
    print k[0], k[1]