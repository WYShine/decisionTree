#encoding:utf-8
from decisionTree import *
#from decisionTree import giniimpurity
from entropy import *
# 决策树的剪枝

my_data=[['slashdot','USA','yes',18,'None'],
        ['google','France','yes',23,'Premium'],
        ['digg','USA','yes',24,'Basic'],
        ['kiwitobes','France','yes',23,'Basic'],
        ['google','UK','no',21,'Premium'],
        ['(direct)','New Zealand','no',12,'None'],
        ['(direct)','UK','no',21,'Basic'],
        ['google','USA','no',24,'Premium'],
        ['slashdot','France','yes',19,'None'],
        ['digg','USA','no',18,'None'],
        ['google','UK','no',18,'None'],
        ['kiwitobes','UK','no',19,'None'],
        ['digg','New Zealand','yes',12,'Basic'],
        ['slashdot','UK','no',21,'None'],
        ['google','UK','yes',18,'Basic'],
        ['kiwitobes','France','yes',19,'Basic']]

def prune(tree,mingain):
    # 如果分支不是叶节点，则对其进行剪枝
    #print(tree.tb)
    #print tree.tb.results;
    if tree.tb.results == None:
        #print "111111"
        prune(tree.tb,mingain)
    if tree.fb.results == None:
        #print "00000"
        prune(tree.fb,mingain)

    # 如果两个子分支都是叶节点，判断是否能够合并
    if tree.tb.results !=None and tree.fb.results !=None:
        #print "2222222"
        #构造合并后的数据集
        tb,fb = [],[]
        for v,c in tree.tb.results.items():
            tb+=[[v]]*c
        for v,c in tree.fb.results.items():
                fb+=[[v]]*c

        #检查熵的减少量
        delta = entropy(tb+fb)-(entropy(tb)+entropy(fb)/2)
        if delta < mingain:
            # 合并分支
            tree.tb,tree.fb = None,None
            tree.results = calUnique(tb+fb)

# test
tree = buildtree(my_data,scoref = giniimpurity)
#print tree.col
#print tree.value
#print tree.results
#print tree.tb
#print tree.fb
prune(tree,0.1)
printtree(tree)