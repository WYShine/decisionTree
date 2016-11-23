#encoding:utf-8
from dataPreProcess import calUnique
def entropy(rows):
	from math import log
	log2 = lambda x:log(x)/log(2)
	results = calUnique(rows)
	#开始计算熵的值
	ent = 0.0
	for r in results.keys():
		p = float(results[r])/len(rows)
		ent = ent - p*log2(p)
	return ent