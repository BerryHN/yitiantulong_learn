# -*- coding: utf-8 -*-
# author:BerryHN
import gensim.models.word2vec  as w2v
import os
base_path = os.path.abspath(os.path.dirname(__file__))
model_file_name = os.path.join(base_path,'../data/ab_model.txt')
file = os.path.join(base_path,'../data/ab_utf_8_segmented.txt')
sentences = w2v.LineSentence(file)
model = w2v.Word2Vec(sentences,size=20,window=5,min_count=5,workers=2)

model.save(model_file_name)

w2v_model = w2v.Word2Vec.load(model_file_name)
print w2v_model.similarity('赵敏'.decode('utf-8'),'赵敏'.decode('utf-8'))
