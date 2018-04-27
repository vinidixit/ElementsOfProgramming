# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 12:36:50 2018

@author: I309535
"""
from BinaryTree import BinaryTreeNode

        
def generateAllBinaryTrees(numNodes):
    result = list()
    
    if numNodes == 0:
        result.append('END')
        
    for numLeftTreeNodes in range(numNodes):
        numRightTreeNodes = numNodes - 1 - numLeftTreeNodes
        leftSubtrees = generateAllBinaryTrees(numLeftTreeNodes)
        rightSubtrees = generateAllBinaryTrees(numRightTreeNodes)
        
        # generate all combinations of left subtrees and right subtrees
        for left in leftSubtrees:
            for right in rightSubtrees:
                result.append(BinaryTreeNode(0, left, right))
                #print result[0].level_order()
        
    return result

trees = generateAllBinaryTrees(2)
print 'no of trees:', len(trees)    

"""
for tree in trees:
    print tree.level_order()
"""

  